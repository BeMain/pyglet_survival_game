from game.gui import gui

import pyglet
from pyglet import app

import glooey


window = pyglet.window.Window()

menu = glooey.Gui(window)
button = gui.Button("Hej på dig du!")

menu.add(button)



app.run()