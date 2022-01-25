from classes.ui import *
from classes.screen import *
from constants import *

button_texts = ["Host Game", "Join Game", "Controls", "Quit"]
button_links = [HOST, JOIN, HOW2PLAY, QUIT]
title_text = Text("Mothership", MEDABOTS, WHITE, [0.5, 0.25], [0.80, 0.80])


buttons = Button.create_buttons(button_texts, GINGA_INTER, DARK_WHITE, WHITE, [0.5, 0.5], [0.33, 0.056], button_links)

elements = []

for button in buttons:
    elements.append(button)
elements.append(title_text)

title = Screen(elements, TITLE, LIGHT_SLATE_GREY)
