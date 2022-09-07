import aiohttp
import urllib.parse
from .schemas import Update

class Command:
    text = ''

    async def run(self, update: Update):
        """method to ovverride"""
        pass


class Webhook:

    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.commands = {cmd.text: cmd for cmd in Command.__subclasses__()}

    async def request(self, method, **params):
        url = self.base_url + method
        if params:
            params_str = '?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)

            url += params_str

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(url) as response:
                return await response.json()

    async def get_me(self):
        info = await self.request('getMe')
        return info

    async def forward_message(self, from_id: int, to_id: int, msg_id: int):
        res = await self.request('forwardMessage', chat_id=to_id, from_chat_id=from_id, message_id=msg_id)
        return res

    async def send_message(self, chat_id: int, message: str):
        res = await self.request('sendMessage', chat_id=chat_id, text=message)
        return res

    async def set_webhook(self, url):
        
        return await self.request('setWebhook', url=url)

    async def delete_webhook(self):
        return await self.request('deleteWebhook')

    async def webhook_info(self):
        info = await self.request('getWebhookInfo')
        print(info)
        return info

    def command(self, fn):
        def wrapper(update: Update, text: str):
            if text == update.message.text:
                return fn(update, text)

        return wrapper