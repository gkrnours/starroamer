import json as JSON

class User(object):
    def __init__(self, cHash, cID, name):
        self._hash = cHash
        self._id = cID
        self.name = name

    @classmethod
    def from_json(cls, json):
        data = JSON.loads(json)
        return cls(
            cHash = data['CharacterOwnerHash'],
            cID   = data['CharacterID'],
            name  = data['CharacterName'],
        )
