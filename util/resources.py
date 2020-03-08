from redis import StrictRedis

from settings import cache_host, cache_port
from dal import CacheManager, PollManager


cache = StrictRedis(host=cache_host, port=cache_port)
cache_manager = CacheManager(cache)
poll_manager = PollManager(cache)
