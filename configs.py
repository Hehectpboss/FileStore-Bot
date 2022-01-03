# (c) @CTP_Official

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_MSG = f"""🤖 **Bot** : CTP Official Bot

👲 **Developer** : [CTP_Official](https://telegram.me/CTP_Official)

📣 **Channel** : @CTP_Official

👥 **Group** : [CTP Discuss Group](https://t.me/CTP_Discuss)

💻 **Source** : [Click here](https://t.me/CTP_Official)

🎧 **Language** : [Python3](https://python.org/)

📚 **Library** : [Pyrogram v1.2.0](https://pyrogram.org/)

🧑‍💻 **Server** : [Heroku](https://heroku.com/)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:[CTP Official](https://t.me/CTP_Official)
"""
	HOME_TEXT = """Hello, [{}](tg://user?id={})

**Iam A Bot Of @CTP_Official. I Will Give You Movie Files**

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [👑CTP Official👑](https://t.me/CTP_Official)
"""
	HELP_TEXT = f"""**Sorry! I Can't Help You**
"""
