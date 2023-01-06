import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5833550185:AAFzUdwF-uiFxIVwzrVS7VepS5GH9tfv0Bk") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 15830858)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "2c015c994c57b312708fecc8a2a0f1a6") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 5884190716)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
