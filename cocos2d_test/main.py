import pyglet
import cocos
from cocos.director import director

class TileMap(cocos.tiles.RectMapLayer):
    def __init__(self, ID, tw, th, cells):
        super(TileMap, self).__init__(ID, tw, th, cells)



director.init(resizable=True)
# Run a scene with our event displayers:
director.run( cocos.scene.Scene(TileMap(0, 100,100,  [["a", "d"], ["b", "e"], ["c", "f"]])))
