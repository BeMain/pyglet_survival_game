import pyglet

from game.objects import lighting

l = lighting.LightHandler()

texture = l.build_lights()
s = pyglet.sprite.Sprite(img=texture, x=0, y=0)

window = pyglet.window.Window()

@window.event
def on_draw():
    s.draw()

pyglet.app.run()