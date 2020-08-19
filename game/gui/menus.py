import pyglet
import glooey

from game import constants
from game.gui import gui


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


class Settings(glooey.Widget, pyglet.event.EventDispatcher):
    #TODO: Add "Back" and "Done" buttons

    Frame = gui.WhiteFrame

    settings = ["SCREEN_WIDTH", "SCREEN_HEIGHT", "FPS"]

    class LabeledInput(glooey.Widget, pyglet.event.EventDispatcher):
        Label = gui.Label
        EditableLabel = gui.EditableLabel

        def __init__(self, setting):
            super().__init__()

            self.register_event_type("on_changed")

            self.setting = setting

            # Create widgets
            hbox = glooey.HBox()
            label = self.Label(self.setting)

            # Create edit label
            edit_label = self.EditableLabel()
            edit_label.text = str(getattr(constants, self.setting))

            @edit_label.event
            def on_unfocus(widget):
                # Set new value
                setattr(constants, self.setting, int(widget.text))

                # Trigger event
                self.dispatch_event("on_changed", self.setting)

            # Add widgets to hbox
            hbox.pack(label)
            hbox.add(edit_label)

            self._attach_child(hbox)
    

    class VBox(glooey.VBox):
        custom_alignment = "center"
        
        custom_cell_alignment = "center"
        custom_cell_padding = 20


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Event
        self.register_event_type("on_setting_changed")

        # Create widgets
        frame = self.Frame()
        vbox = self.VBox()

        for setting in self.settings:
            label = self.LabeledInput(setting)
            label.push_handlers(on_changed=lambda s: self.dispatch_event("on_setting_changed", s))
                
            vbox.add(label)

        # Add widgets
        frame.add(vbox)
        self._attach_child(frame)
