import pyglet


class PhysicsObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicsObject, self).__init__(*args, **kwargs)

        self.event_handlers = []

        self.velx = 0.0
        self.vely = 0.0

    def update(self):
        self.x += self.velx
        self.y += self.vely
