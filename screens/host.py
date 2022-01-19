from classes.ui import *
from classes.screen import *
from constants import *

title_text = Text("Host Game", MEDABOTS, WHITE, [0.5, 0.10], [0.60, 0.60])
# username_text = Text("Username", GINGA_INTER, WHITE, [0.5, 0.5], [0.4, 0.4])
name_box = InputBox(GINGA_INTER, [0.5, 0.5], [0.4, 0.4])

elements = []
elements.append(title_text)
elements.append(name_box)

host = Screen(elements, HOST, LIGHT_SLATE_GREY)