# CleverDiscordChatbots
Two simple Discord chatbots with the ability to react on each other.

### These are the prerequisites you need:
- Python 3 (preferably 3.6)
- The following libraries: discord.py, asyncio, aiohttp, googletrans, json and requests (to install them type the following in your command prompt for each library 'pip install LIBRARY_TO_INSTALL')
- 2 discord bot tokens (here's a simple guide: https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
- The discord client ID's of your bots and yourself (https://discordia.me/developer-mode, after enabling developer mode simply right click on yourself in the memberlist and select 'Copy ID')
- A https://cleverbot.io/ account. After making one you need a key and username for your cleverbot, which can be found here https://cleverbot.io/keys. You can use the same account for both bots.

### Setup
Before you start the bots you have to edit the variables at the start of bot1.py and bot2.py and add the information you've acquired in the previous steps. You can use the same cleverbot username and key for both files, but you need two separate bot tokens. Lastly, you need to pick a name for the destination text channel or just make a new text channel in your server with the name 'bikini_bottom'.
For example:

Bot1.py
```
Token = "NIDOWpa9wpidawdaa.DJWAIoa.ahUIDHWId89WDa7dawd7dwauoid7daw78dw"
bot1_id = "431897473129847213"
bot2_id = "341897419874382974"
owner_id = "431439180483120431"
clever_user = 'DOWmoWodWLdLWdml'
clever_key = 'RWA567DWAYuoidwAAwdjoia23'
chat_channel = 'bikini_bottom'
cleverbotname = 'Spongebot'
```

Bot2.py
```
Token = "AHWDoiJIwodajnoidawd.Ajwidajdwa.dahwuidbhawDWUAIhda8WAadwDdwadj"
bot1_id = "431897473129847213"
bot2_id = "341897419874382974"
owner_id = "431439180483120431"
clever_user = 'DOWmoWodWLdLWdml'
clever_key = 'RWA567DWAYuoidwAAwdjoia23'
chat_channel = 'bikini_bottom'
cleverbotname = 'Patbot'
```

Now it's time to run the bots! Go to your command prompt and open two separate windows; one for each bot. Type the following in both windows to change to the bot directory:

_Windows:_
```
cd C:\path\to\bots
```
_Linux:_
```
cd ~/path/to/bots
```

Next, type this in one of the windows:

_Windows:_
```
python bot1.py
```
_Linux:_
```
python3 bot1.py
```
and do the same thing for bot2.py.

Your bots are now online! You can start the conversation by sending a message in 'bikini_bottom' or whatever you've called it. The bots will ignore all members except for themselves and yourself, so don't send any further messages, because it will mess up the bots.

Have fun and let me know if you encounter bugs or issues (trust me, you will)! Here are a few example screenshots from my own server: https://www.reddit.com/r/discordapp/comments/8imutl/i_programmed_two_discord_bots_to_react_on_each/

### Useful links and credits:
- http://discordpy.readthedocs.io/en/latest/api.html
- https://github.com/jagrosh/FrostCleverbot