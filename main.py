import urllib.parse
import os
from fastapi import FastAPI
from tg.schemas import Update
from tg.obj import bot
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

token = urllib.parse.quote(os.getenv('BOT_TOKEN').split(':')[1])

@app.get('/debug')
async def debug():
    return 'Its Worked!'


@app.post(f"/{token}/update")
async def webhook(update: Update):
    pass

@app.on_event("startup")
async def startup_event():
    res = await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/{token}/update")
    print(res)


@app.on_event("shutdown")
async def shutdown_event():
    res = await bot.delete_webhook()
    print(res)