from sanic import Sanic


app = Sanic()


app_host = '0.0.0.0'
app_port = 8000
app_workers = 4

cache_host = 'localhost'
cache_port = 6379 # default
