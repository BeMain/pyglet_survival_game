import pyglet
from pyglet.window import key

window = pyglet.window.Window()

label = pyglet.text.Label(
    "Hello, world", font_name="Times New Roman", font_size=36, x=window.width//2, y=window.height//2, anchor_x="center", anchor_y="center")
image = pyglet.resource.image("textures/tree.jpeg")


#event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        print(chr(symbol))


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button)


@window.event
def on_draw():
    window.clear()
    # label.draw()
    #image.blit(0, 0)

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 0, 2, 3],
                                 ('v2i', (100, 100,
                                          150, 100,
                                          150, 150,
                                          100, 150))
                                 )


if __name__ == "__main__":
    pyglet.app.run()
