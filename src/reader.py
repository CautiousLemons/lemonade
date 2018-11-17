import json


class Reader:
    def __init__(self):
        pass

    def readJSON(self, file):
        with open(file) as f:
            data = json.load(f)
        return data
