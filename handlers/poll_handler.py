from handlers import BaseHandler
from models import Vote


class PollHandler(BaseHandler):
    async def get(self, request):
        votes = await self.dal.get_all_votes()
        rendered = [vote.render() for vote in votes]
        return await self.write_json(rendered)

    async def post(self, request):
        vote = Vote.load_from_doc(request.body)
        result = await self.dal.create_vote_for_user(vote)
        return await self.write_json(result)


class ExamplePollHandler(BaseHandler):
    async def get(self, request):
        return await self.write_json(Vote.example())
