# imports
from classes.ui import *
from classes.screen import *
from constants import *
from ipcoder import get_code
from random import randint

# create elements
title_text = Text("Host Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
code_text = Text(get_code(CLIENT_IP, randint(0, 255)), GINGA_INTER, GREEN, [0.5, 0.4], [0.75, 0.2])
share_text = Text("Share this code with your friend to start a match!", GINGA_INTER, GREY, [0.5, 0.57], [0.75, 0.2])
back_button = Button("Back", GINGA_INTER, DARK_WHITE, WHITE, [0.05, 0.05], [0.1, 0.1], TITLE)

# append elements to list
elements = []
elements.append(title_text)
elements.append(code_text)
elements.append(share_text)
elements.append(back_button)

# create screen object
host = Screen(elements, HOST, LIGHT_SLATE_GREY)