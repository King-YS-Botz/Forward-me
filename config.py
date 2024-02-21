from os import environ  
  
class Config:
     API_ID = int(environ.get("API_ID", "21444884")) 
     API_HASH = environ.get("API_HASH", "9e753c5184d9dbf3ee10d1ce299dd882") 
     BOT_TOKEN = environ.get("BOT_TOKEN", "6891330421:AAHxzAso1-TxVdS7ZTZjeUIE9D0psTC2g4s")  
     BOT_SESSION = environ.get("BOT_SESSION", "bot")  
     DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Armour:uxT6MLCPGf3WuDWl@armour.zlx7omm.mongodb.net/?retryWrites=true&w=majority") 
     DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0") 
     BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6885764469').split()] 
  
class temp(object): 
     lock = {} 
     CANCEL = {} 
     forwardings = 0 
     BANNED_USERS = [] 
     IS_FRWD_CHAT = [] 
 
