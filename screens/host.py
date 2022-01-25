from classes.ui import *
from classes.screen import *
from constants import *
from ipcoder import get_code
from random import randint

button_texts = ["2 Players", "4 Players"]
bl = [0, 0]
back_text = ["Back",]
bl2 = [0,]
title_text = Text("Host Game", MEDABOTS, WHITE, [0.5, 0.05], [0.25, 0.25])
code_text = Text(get_code(CLIENT_IP, randint(0, 255)), GINGA_INTER, GREEN, [0.5, 0.4], [0.75, 0.2])
share_text = Text("Share this code with your friend to start a match!", GINGA_INTER, GREY, [0.5, 0.57], [0.75, 0.2])

elements = []
elements.append(title_text)
elements.append(code_text)
elements.append(share_text)

host = Screen(elements, HOST, LIGHT_SLATE_GREY)