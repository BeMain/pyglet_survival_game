import glooey

class Label(glooey.Label):
    custom_font_size = 20
    custom_color = '#b9ad86'
    custom_alignment = 'center'

class Button(glooey.Button):
    Foreground = Label
