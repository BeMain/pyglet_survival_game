import glooey

from game.gui import menus


class GuiHandler(glooey.Gui):
    def open_menu(self):
        menu = menus.MainMenu()
        
        @menu.event
        def on_button_click(action):
            if action == "Continue":
                self.get_window().set_paused(False)
            elif action == "Exit":
                self.get_window().exit()

            else: 
                print("Unknown action:", action)

        self.add(menu)