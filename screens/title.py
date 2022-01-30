# imports
from classes.ui import *
from classes.screen import *
from constants import *

# create elements
title_text = Text("Mothership", MEDABOTS, WHITE, [0.5, 0.25], [0.80, 0.80])
button_texts = ["Host Game", "Join Game", "Controls", "Quit"]
button_links = [HOST, JOIN, HOW2PLAY, QUIT]
buttons = Button.create_buttons(button_texts, GINGA_INTER, DARK_WHITE, WHITE, [0.5, 0.5], [0.33, 0.056], button_links)

# append elements to list
elements = []
for button in buttons:
    elements.append(button)
elements.append(title_text)

# create screen object
title = Screen(elements, TITLE, LIGHT_SLATE_GREY)
