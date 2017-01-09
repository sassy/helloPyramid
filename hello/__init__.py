from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('hello', '/')
    config.add_route('home', '/home')
    config.add_route('home2', '/home2')
    config.add_route('home3', '/home3')
    config.scan('.views')
    config.add_route('api', '/api/*traverse')
    config.scan('.apis')
    return config.make_wsgi_app()
