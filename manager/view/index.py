import aiohttp_jinja2
from aiohttp.web_urldispatcher import View


class IndexView(View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return {'name': 'RaspManager'}
