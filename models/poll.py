import json
from uuid import UUID, uuid4


class Vote:
    def __init__(self, poll_id, upvote, user_id):
        self.poll_id = poll_id
        self.upvote = upvote
        self.user_id = user_id

    @property
    def poll_id_str(self):
        return str(self.poll_id)

    @property
    def user_id_str(self):
        return str(self.user_id)

    @classmethod
    def load_from_doc(cls, doc):
        if isinstance(doc, bytes):
            doc = doc.decode('utf-8')
            doc = json.loads(doc)
        print(doc.get('upvote'))
        return cls(
            UUID(doc.get('poll_id')),
            bool(doc.get('upvote')),
            UUID(doc.get('user_id'))
        )

    def render(self):
        return {
            'poll_id': str(self.poll_id),
            'upvote': self.upvote,
            'user_id': str(self.user_id)
        }

    def serialize(self):
        return json.dumps(self.render())

    @classmethod
    def example(cls):
        obj = cls(
            uuid4(),
            True,
            uuid4(),
        )
        return obj.render()
