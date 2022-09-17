import urllib.parse
import os
from fastapi import FastAPI
from tg.schemas import Update
from tg.obj import bot
from strapi.api import Strapi
from bot_logic import ctx

strapi = Strapi(os.getenv('STRAPI_URL'), os.getenv('STRAPI_API_KEY'))
app = FastAPI()
token = urllib.parse.quote(os.getenv('BOT_TOKEN').split(':')[1])

@app.get('/debug')
async def debug():
    data ={
        "text": "Testiiiiing",
        "sender_tid": 12372348,
        "message_id": 87652344321
    }

    rs = await strapi.create_post(data)
    return rs

@app.post(f"/{token}/update")
async def webhook(update: Update):
    ctx.build_context(update)
    # build_context(update)
    # data = {
    #     'text': update.message.text,
    #     'sender_tid': update.message.chat.id,
    #     'message_id': update.message.message_id
    # }
    # rs = await strapi.create_post(data)
    print('ok')


@app.on_event("startup")
async def startup_event():
    #res = await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/{token}/update")
    res = await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/{token}/update")

    print(res)


@app.on_event("shutdown")
async def shutdown_event():
    res = await bot.delete_webhook()
    print(res)