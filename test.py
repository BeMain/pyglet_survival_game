from game.gui import gui

import pyglet
from pyglet import app

import glooey


window = pyglet.window.Window()

menu = glooey.Gui(window)
menu.add(gui.Button("Hej!"))



app.run()