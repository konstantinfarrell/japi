from dal import CacheManager
from models import Vote


class PollManager(CacheManager):
    def __init__(self, *args, **kwargs):
        self.cache_key = 'poll:{}:{}'
        super().__init__(*args, **kwargs)

    async def get_all_votes(self):
        key = self.cache_key.replace('{}:{}', '{}').format('*')
        all_keys = self.keys(key)
        results = [self.get(k) for k in all_keys]
        results = [Vote.load_from_doc(doc) for doc in results]
        return results

    async def get_all_votes_for_poll(self, poll_id):
        key = self.cache_key.format(poll_id, '*')
        all_keys = self.keys(key)
        results = [self.get(k) for k in all_keys]
        results = [Vote.load_from_doc(doc) for doc in results]
        return results

    async def get_all_votes_for_user(self, poll_id, user_id):
        key = self.cache_key.format(poll_id, user_id)
        result = self.get(key)
        return result

    async def create_vote_for_user(self, vote):
        key = self.cache_key.format(vote.poll_id_str, vote.user_id_str)
        serialized = vote.serialize()
        self.set(key, serialized)
        return serialized
