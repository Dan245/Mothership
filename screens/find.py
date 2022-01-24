from classes.ui import *
from classes.screen import *
from constants import *

title_text = Text("Join Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
input_box = InputBox("Enter Room Code", GINGA_INTER, [0.5, 0.5], [0.75, 0.25])

button_texts = ["Join Game",]
buttons = Button.create_buttons(button_texts, GINGA_INTER, WHITE, WHITE, [0.5, 0.9], [0.2, 0.16])

elements = []
elements.append(title_text)
elements.append(input_box)
for button in buttons:
    elements.append(button)

joinn = Screen(elements, JOIN, LIGHT_SLATE_GREY)