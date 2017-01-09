from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='hello', renderer='home.pt')
def hello_world2(request):
    print('Incomming request')
    return {"name" : 'Hello World!'}

@view_config(route_name='home')
def home(request):
    return Response('Welcome!')

@view_config(route_name='home2', renderer='home.pt')
def home2(request):
    return {"name": "test"}
