# CleverDiscordChatbots
Two simple Discord chatbots with the ability to react on each other.

These are the prerequisites you need to be able to run these bots:
- Python 3 (preferably 3.6)
- The following libraries: discord.py, asyncio, aiohttp, googletrans, json and requests (to install them type the following in your command prompt for each library 'pip install LIBRARY_TO_INSTALL')
- 2 discord bot tokens (here's a simple guide: https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
- The discord client ID's of your bots and yourself (https://discordia.me/developer-mode, after enabling developer mode simply right click on yourself in the memberlist and select 'Copy ID')
- A https://cleverbot.io/ account. After making one you need a key and username for your cleverbot, which can be found here https://cleverbot.io/keys. You can use the same account for both bots.

Before you start the bots you have to edit the variables at the start of bot1.py and bot2.py and add the information you've acquired in the previous steps. You can use the same cleverbot username and key for both files, but you need two separate bot tokens.
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
