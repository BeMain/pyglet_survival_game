import pyglet

from . import constants, util


class PhysicsObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicsObject, self).__init__(*args, **kwargs)

        self.event_handlers = []

        self.velx = 0.0
        self.vely = 0.0

    def update(self):
        self.x += self.velx
        self.y += self.vely

        self.check_bounds()

    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = constants.SCREEN_WIDTH
        max_y = constants.SCREEN_HEIGHT

        self.x = util.clamp(self.x, min_x, max_x)
        self.y = util.clamp(self.y, min_y, max_y)
