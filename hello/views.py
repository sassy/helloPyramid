from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='hello', renderer='string')
def hello_world(request):
    return 'Hello World'

@view_config(route_name='hello2')
def hello_world2(request):
    print('Incomming request')
    return Response('<body><h1>Hello World!</h1></body>')

@view_config(route_name='home')
def home(request):
    return Response('Welcome!')

@view_config(route_name='home2', renderer='json')
def home2(request):
    return {"a": 1, "b": 2}
