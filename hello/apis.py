from pyramid.view import view_config, view_defaults

@view_defaults(route_name='api')
class HelloApis:
    def __init__(self, request):
        self.request = request

    @view_config(name='', renderer='json')
    def hello(request):
        return {"hello": "world"}

    @view_config(name='name', renderer='json')
    def hello_world(self):
        return {"name": "sassy"}
