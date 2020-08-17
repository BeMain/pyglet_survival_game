import pyglet
import glooey

from game import constants
from game.gui import gui

class MainMenu(glooey.Bin, pyglet.event.EventDispatcher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Event
        self.register_event_type("on_button_click")

        frame = gui.WhiteFrame()

        # Create VBox
        vbox = glooey.VBox(3)
        vbox.alignment = "center"
        
        vbox.cell_alignment = "center"
        vbox.cell_padding = 20

        # Create buttons
        btn_continue = gui.Button("Continue")
        btn_settings = gui.Button("Settings")
        btn_exit = gui.Button("Exit")

        # Handlers
        @btn_continue.event
        def on_click(widget):
            self.dispatch_event("on_button_click", "continue")

        @btn_settings.event
        def on_click(widget):
            self.dispatch_event("on_button_click", "settings")
        
        @btn_exit.event
        def on_click(widget):
            self.dispatch_event("on_button_click", "exit")

        # Add buttons
        vbox.add(btn_continue)
        vbox.add(btn_settings)
        vbox.add(btn_exit)


        frame.add(vbox)

        self.add(frame)
