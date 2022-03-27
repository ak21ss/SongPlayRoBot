import os
API_ID = int(os.getenv("11341733"))
API_HASH = os.getenv("a8d0e82a1d69196c018caeacc6ee389f") 
BOT_TOKEN = os.getenv("5234085443:AAH3QO_7ynvsZNDinpiyE-UVOpfuISmXJyA")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
