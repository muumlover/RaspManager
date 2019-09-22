import aiohttp_jinja2
import jinja2
from aiohttp import web

from manager.view.error import ErrorView
from manager.view.index import IndexView
from manager.view.login import LoginView
from manager.view.welcome import WelcomeView


async def handler(request):
    location = request.app.router['index'].url_for()
    raise web.HTTPFound(location=location)


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./manager/templates'))
app.router.add_static('/static', './manager/templates/static')

app.router.add_get('/', handler)
app.router.add_view('/login', LoginView, name='login')
app.router.add_view('/index', IndexView, name='index')
app.router.add_view('/error', ErrorView, name='error')

app.router.add_view('/welcome', WelcomeView, name='welcome')

if __name__ == '__main__':
    web.run_app(app)
