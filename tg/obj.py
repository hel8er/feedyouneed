import os
from dotenv import load_dotenv
from .webhook import Webhook
load_dotenv()
bot = Webhook(os.getenv('BOT_TOKEN'))

