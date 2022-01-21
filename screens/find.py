from classes.ui import *
from classes.screen import *
from constants import *

title_text = Text("Join Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
input_box = InputBox("Enter Room Code", GINGA_INTER, [0.5, 0.5], [0.75, 0.25])

elements = []
elements.append(title_text)
elements.append(input_box)

joinn = Screen(elements, JOIN, LIGHT_SLATE_GREY)