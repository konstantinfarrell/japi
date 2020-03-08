import json

from sanic.views import HTTPMethodView
from sanic.response import json as sjson, text


class BaseHandler(HTTPMethodView):
    def __init__(self, dal, *args, **kwargs):
        self.dal = dal

    async def get(self, request):
        return await self.bad_request()

    async def post(self, request):
        return await self.bad_request()

    async def bad_request(self, message='Bad Request'):
        return text(body=message, status=400)

    async def not_authorized(self, message='Not Authorized'):
        return text(body=message, status=401)

    async def write_json(self, doc):
        if isinstance(doc, str):
            doc = json.loads(doc)
            return sjson(body=doc, status=200)
        return sjson(body=doc, status=200)
