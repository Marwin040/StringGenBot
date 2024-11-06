from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("26655243"))
API_HASH = getenv("535a90f092149e8173be6c41a9fd5577")

BOT_TOKEN = getenv("7264357275:AAEsKOhuIRMKacIIDFGowJ1PfSkqcAPDlKM")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://marwinalone2002:0PxKXvOj7tByYpoD@cluster0.jmljy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 8194005351))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tamilchat_alapparai")
