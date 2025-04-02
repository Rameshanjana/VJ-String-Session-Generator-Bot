from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "10379650"))
API_HASH = environ.get("API_HASH", "29813216c8daa138b7abbb3df3012c35")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "1182181055")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://vk5347775:nl8OheOy2CyF9Vz6@cluster0.rvbwqdr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
