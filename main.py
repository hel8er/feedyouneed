import urllib.parse
import os
from fastapi import FastAPI
from tg.schemas import Update
from tg.obj import bot
from dotenv import load_dotenv
from strapi.api import Strapi
from tg.context import webhook, build_context
from pyngrok import ngrok
import bot_logic

def start_ngrok():
    [ngrok.disconnect(t.public_url) for t in ngrok.get_tunnels()]
    #print(ngrok.get_tunnels())
    http_tunnel = ngrok.connect(8000)
    url = ngrok.get_tunnels()[0].public_url
    print(url)
    return url
    
strapi = Strapi(os.getenv('STRAPI_URL'), os.getenv('STRAPI_API_KEY'))
load_dotenv()
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
# @webhook
async def webhook(update: Update):
    build_context(update)
    # data = {
    #     'text': update.message.text,
    #     'sender_tid': update.message.chat.id,
    #     'message_id': update.message.message_id
    # }
    # rs = await strapi.create_post(data)
    # print(rs)


@app.on_event("startup")
async def startup_event():
    #res = await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/{token}/update")
    res = await bot.set_webhook(f"{start_ngrok()}/{token}/update")

    print(res)


@app.on_event("shutdown")
async def shutdown_event():
    ngrok.kill()
    res = await bot.delete_webhook()
    print(res)