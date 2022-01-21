from classes.ui import *
from classes.screen import *
from constants import *

button_texts = ["2 Players", "4 Players"]
back_text = ["Back",]
title_text = Text("Host Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
buttons = Button.create_buttons(button_texts, GINGA_INTER, WHITE, WHITE, [0.5, 0.5-0.33/4], [0.33, 0.2])
buttons2 = Button.create_buttons(back_text, GINGA_INTER, WHITE, WHITE, [0.05, 0.05], [0.1, 0.1])

elements = []
elements.append(title_text)
elements.append(buttons2[0])
for button in buttons:
    elements.append(button)

host = Screen(elements, HOST, LIGHT_SLATE_GREY)