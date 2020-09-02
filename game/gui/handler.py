import glooey

from game import constants
from game.gui import menus, pause


class GuiHandler(glooey.Gui):
    def __init__(self, *args, **kwargs):
        super(GuiHandler, self).__init__(*args, **kwargs)
        
        self.menus = []

    def close_menus(self):
        pause.paused = False
        self.clear()
        self.menus = []

    def open_main_menu(self):
        menu = menus.MainMenu()
        self.menus.append(menu)
        
        @menu.event
        def on_button_click(action):
            if action == "Continue":
                self.close_menus()
            elif action == "Settings":
                self.open_settings()
            elif action == "Exit":
                self.get_window().exit()

            else: 
                print("Unknown action:", action)

        self.clear()
        self.add(menu)

        pause.paused = True
    
    def open_settings(self):
        menu = menus.Settings()

        @menu.event
        def on_setting_changed(setting):
            if setting == "SCREEN_HEIGHT":
                self.get_window().height = constants.SCREEN_HEIGHT
            elif setting == "SCREEN_WIDTH":
                self.get_window().width = constants.SCREEN_WIDTH
        
        @menu.event
        def on_button_click(action):
            if action == "Back":
                self.open_main_menu()
            if action == "Done":
                self.close_menus()

        self.clear()
        self.add(menu)

        
