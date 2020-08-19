import glooey

from game import constants
from game.gui import menus


class GuiHandler(glooey.Gui):
    def open_menu(self):
        menu = menus.MainMenu()
        
        @menu.event
        def on_button_click(action):
            if action == "Continue":
                self.get_window().set_paused(False)
            elif action == "Settings":
                self.open_settings()
            elif action == "Exit":
                self.get_window().exit()

            else: 
                print("Unknown action:", action)
        
        self.clear()
        self.add(menu)
    
    def open_settings(self):
        menu = menus.Settings()

        @menu.event
        def on_setting_changed(setting):
            if setting == "SCREEN_HEIGHT":
                self.get_window().height = constants.SCREEN_HEIGHT
            elif setting == "SCREEN_WIDTH":
                self.get_window().width = constants.SCREEN_WIDTH


        self.clear()
        self.add(menu)

        
