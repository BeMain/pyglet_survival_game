from game.gui import gui, menu

import pyglet
from pyglet import app

import glooey


window = pyglet.window.Window()

menu = menu.MainMenu(window)




app.run()