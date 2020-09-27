import pyglet
from pyglet.gl import *

from game import constants, resources


class Light():
    def __init__(self, x, y, radius, color=[0,0,0,0]):
        super().__init__()

        # Setup image
        self.image = self.init_image()

        self.radius = radius
        self.color = color

        self.x = x
        self.y = y
    
    def init_image(self):
        image = resources.light_dimmed
        return image


class LightHandler:
    def __init__(self):
        super().__init__()

        self.player_light = Light(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2, 10)

    def build_lights(self):
        # Background
        bg_pattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
        bg = pyglet.image.create(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, pattern=bg_pattern)

        bg.get_texture().blit_into(self.player_light.image.get_image_data(), self.player_light.x, self.player_light.y, 0)

        return bg
    
    def draw(self):
        self.build_lights().blit(0,0)
    