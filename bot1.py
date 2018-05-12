import asyncio
import discord
import aiohttp
from discord.ext import commands
import requests
import json

bot = commands.Bot(description="chatbot 1", command_prefix="")

Token = "BOT2_TOKEN"
bot1_id = "CLIENT_ID_FIRST_BOT"
bot2_id = "CLIENT_ID_SECOND_BOT"
owner_id = "YOUR_OWN_CLIENT_ID"
clever_user = 'USERNAME_CLEVERBOT'
clever_key = 'KEY_CLEVERBOT'
chat_channel = 'bikini_bottom'
cleverbotname = 'Spongebot'

@bot.event
async def on_message(msg):
	botmember = msg.server.get_member(bot1_id)
	try:
		if msg.author != botmember and (msg.server == None or (msg.channel.name == chat_channel and msg.author == msg.server.get_member(bot2_id))):
			await bot.send_typing(msg.channel)
			txt = msg.content.replace(msg.server.me.mention,'') if msg.server or msg.channel.name != chat_channel else msg.content
			async with aiohttp.ClientSession() as session:
				async with session.post('https://cleverbot.io/1.0/ask', data={'user':clever_user, 'key':clever_key, 'nick':cleverbotname, 'text':txt}) as resp:
					r = await resp.json()
					if r['status'] == 'success':
						await bot.send_message(msg.channel, r['response'] )
	except Exception as e:
		print("Error: " + str(e))
		await bot.send_message(msg.channel, "I had an error and I don't care")

requests.post('https://cleverbot.io/1.0/create', json={'user':clever_user, 'key':clever_key, 'nick':cleverbotname})
bot.run(Token)