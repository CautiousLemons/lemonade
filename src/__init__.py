from src.reader import Reader
from src.renderer import Renderer

reader = Reader()
renderer = Renderer()

config = reader.readJSON("../sample.json")
renderer.render(config)
