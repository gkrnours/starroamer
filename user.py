import json as JSON

class User(object):
    def __init__(self, cHash, cID, name):
        self._hash = cHash
        self._id = cID
        self.name = name

    def __getstate__(self):
        return {"hash":self._hash, "id":self._id, "name":self.name}

    @classmethod
    def __setstate__(cls, state):
        return cls(
            cHash = state["hash"],
            cID   = state["id"],
            name  = state["name"]
        )

    @classmethod
    def from_json(cls, json):
        data = JSON.loads(json)
        return cls(
            cHash = data['CharacterOwnerHash'],
            cID   = data['CharacterID'],
            name  = data['CharacterName'],
        )
