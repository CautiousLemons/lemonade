import json

class Reader:
    def __init__(self):
        print("Instantiating Reader class")

    def readJSON(self, file):
        with open(file) as f:
            data = json.load(f)
        return data

r1 = Reader()
data = r1.readJSON("../sample.json")
print data["nodes"][1]