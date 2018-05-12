import asyncio
import discord
import aiohttp
from discord.ext import commands
from googletrans import Translator
import requests
import json

bot = commands.Bot(description="chatbot 2", command_prefix="")
translator = Translator()


Token = "BOT1_TOKEN"
bot1_id = "CLIENT_ID_FIRST_BOT"
bot2_id = "CLIENT_ID_SECOND_BOT"
owner_id = "YOUR_OWN_CLIENT_ID"
clever_user = 'USERNAME_CLEVERBOT'
clever_key = 'KEY_CLEVERBOT'
chat_channel = 'bikini_bottom'
cleverbotname = 'Patbot'


@bot.event
async def on_message(msg):
	botmember = msg.server.get_member(bot2_id)
	ownermember = msg.server.get_member(owner_id)
	try:
		if msg.author != botmember and (msg.server == None or (msg.channel.name == chat_channel and (msg.author == msg.server.get_member(bot1_id) or msg.author == ownermember))):
			await bot.send_typing(msg.channel)
			txt = msg.content.replace(msg.server.me.mention,'') if msg.server or msg.channel.name != chat_channel else msg.content
			async with aiohttp.ClientSession() as session:
				async with session.post('https://cleverbot.io/1.0/ask', data={'user':clever_user, 'key':clever_key, 'nick':cleverbotname, 'text':txt}) as resp:
					r = await resp.json()
					if r['status'] == 'success':
						if translator.detect(r['response']).lang != 'en' or translator.detect(r['response']).lang != 'nl':
							reply = translator.translate(r['response'], dest='en').text
						else:
							pass
						if reply == msg.content:
							await bot.send_message(msg.channel, "loop alert, but don't worry")
						else:
							await bot.send_message(msg.channel, reply)
	except Exception as e:
		print("Error: " + str(e))
		await bot.send_message(msg.channel, "I had an error, but I don't care")

requests.post('https://cleverbot.io/1.0/create', json={'user':clever_user, 'key':clever_key, 'nick':cleverbotname})
bot.run(Token)