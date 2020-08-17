from game.gui import gui, main_menu

import pyglet
from pyglet import app

import glooey


window = pyglet.window.Window()
gui = gui.GuiHandler(window)

gui.open_menu()



app.run()