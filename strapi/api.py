import httpx


class Strapi:

    def __init__(self, url: str, token: str):
        self.token = token
        self.url = url
        self.client = httpx.AsyncClient(headers={'Authorization': 'Bearer ' + token})

    async def create_post(self, data: dict):
        json = {"data": data}
        rs = await self.client.post(self.url+'/api/posts', json=json)
        return rs.json()