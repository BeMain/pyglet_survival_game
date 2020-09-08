import pyglet
import glooey

from game.gui import inventory


window = pyglet.window.Window()
gui = glooey.Gui(window)

inv = inventory.Inventory()
gui.add(inv)

pyglet.app.run()