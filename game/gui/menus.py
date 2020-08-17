import pyglet
import glooey

#from game import constants
from game.gui import gui

print(gui.WhiteFrame())

class MainMenu(glooey.Widget, pyglet.event.EventDispatcher):
    Frame = gui.WhiteFrame
    Button = gui.Button
    actions = ["Continue", "Settings", "Exit"]

    custom_alignment = "center"

    class VBox(glooey.VBox):
        custom_alignment = "center"
        
        custom_cell_alignment = "center"
        custom_cell_padding = 20


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Event
        self.register_event_type("on_button_click")

        # Create widgets
        frame = self.Frame()
        vbox = self.VBox()
        
        # Create buttons
        for action in self.actions:
            vbox.add(self._button(action))

        # Add widgets
        frame.add(vbox)
        self._attach_child(frame)
    
    def _button(self, action):
        button = self.Button(action)

        @button.event
        def on_click(widget):
            self.dispatch_event("on_button_click", action)

        return button


class Settings(glooey.Bin, pyglet.event.EventDispatcher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
