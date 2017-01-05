from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='hello', renderer='string')
def hello_world(request):
    return 'Hello World'

def hello_world2(request):
    print('Incomming request')
    return Response('<body><h1>Hello World!</h1></body>')

@view_config(route_name='home')
def home(request):
    return Response('Welcome!')

@view_config(route_name='home2', renderer='json')
def home2(request):
    return {"a": 1, "b": 2}

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_route('home', '/home')
    config.add_route('home2', '/home2')
    config.add_route('hello2', '/hello2')
    config.add_view(hello_world2, route_name='hello2')
    config.scan('.')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8001, app)
    server.serve_forever()
