from settings import app
from handlers import BaseHandler, PollHandler, ExamplePollHandler
from util.resources import cache_manager, poll_manager


ROUTES = [
    (BaseHandler, '/', cache_manager),
    (PollHandler, '/poll', poll_manager),
    (ExamplePollHandler, '/poll/example', poll_manager),
]

for route in ROUTES:
    app.add_route(route[0].as_view(route[2]), route[1])
