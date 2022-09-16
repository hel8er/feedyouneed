import os
from dotenv import load_dotenv
from .webhook import Webhook
from context.core import Context
load_dotenv()
bot = Webhook(os.getenv('BOT_TOKEN'))
ctx = Context()
