import urllib.parse
import os
from fastapi import FastAPI
from tg.schemas import Update
from tg.obj import bot
from dotenv import load_dotenv
from strapi.api import Strapi

from pyngrok import ngrok

def start_ngrok():
    [ngrok.disconnect(t.public_url) for t in ngrok.get_tunnels()]
    #print(ngrok.get_tunnels())
    http_tunnel = ngrok.connect(8000)
    return ngrok.get_tunnels()[0].public_url

print('start', start_ngrok())
ngrok.kill()
print('after kill', ngrok.get_tunnels())
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
async def webhook(update: Update):
    if update.message.text and not update.message.text.startswith('/'):
        data = {
            'text': update.message.text,
            'sender_tid': update.message.chat.id,
            'message_id': update.message.message_id
        }
        rs = await strapi.create_post(data)
        print(rs)

@app.on_event("startup")
async def startup_event():
    ngrok_url = start_ngrok()
    res = await bot.set_webhook(f"{ngrok_url}/{token}/update")
    print(res)


@app.on_event("shutdown")
async def shutdown_event():
    ngrok.kill()
    res = await bot.delete_webhook()
    print(res)