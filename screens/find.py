# imports
from classes.ui import *
from classes.screen import *
from constants import *

# create ui elements
title_text = Text("Join Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
input_box = InputBox("Enter Room Code", GINGA_INTER, [0.5, 0.5], [0.75, 0.25])
back_button = Button("Back", GINGA_INTER, DARK_WHITE, WHITE, [0.05, 0.05], [0.1, 0.1], TITLE)
join_button = Button("Join", GINGA_INTER, WHITE, WHITE, [0.5, 0.9], [0.2, 0.16], GAME)

# append ui elements to list
elements = []
elements.append(title_text)
elements.append(input_box)
elements.append(join_button)
elements.append(back_button)

# create screen object
joinn = Screen(elements, JOIN, LIGHT_SLATE_GREY)