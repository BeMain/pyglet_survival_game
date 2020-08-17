import glooey

from game import constants
from game.gui import gui

class MainMenu(glooey.Gui):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

        frame = gui.WhiteFrame()

        vbox = glooey.VBox(3)
        vbox.alignment = "center"
        
        vbox.cell_alignment = "center"
        vbox.cell_padding = 20

        vbox.add(gui.Button("Continue"))
        vbox.add(gui.Button("Settings"))
        vbox.add(gui.Button("Exit"))

        frame.add(vbox)

        self.add(frame)
