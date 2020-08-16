import glooey

from game.gui import resources

class WhiteBorder(glooey.images.Background):
    custom_top = resources.white_border["top"]
    custom_bottom = resources.white_border["bottom"]
    custom_right = resources.white_border["right"]
    custom_left = resources.white_border["left"]

    custom_top_right = resources.white_border["tr"]
    custom_top_left = resources.white_border["tl"]
    custom_bottom_right = resources.white_border["br"]
    custom_bottom_left = resources.white_border["bl"]


class Label(glooey.Label):
    custom_font_size = 20
    custom_color = '#b9ad86'
    custom_alignment = 'center'

class Button(glooey.Button):
    Foreground = Label
    Background = WhiteBorder
