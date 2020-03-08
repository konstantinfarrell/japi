class CacheManager:
    def __init__(self, client):
        self.client = client

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value)

    def keys(self, key):
        return self.client.keys(key)
