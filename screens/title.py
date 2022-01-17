from classes.ui import *
from classes.screen import *
from constants import *
import pygame

button_texts = ["Host Game", "Find Game", "Options", "How to Play", "Quit"]
title_text = Text("Mothership", MEDABOTS, WHITE, [0.5, 0.25], [0.80, 0.80])


buttons = Button.create_buttons(button_texts, GINGA_INTER, WHITE, WHITE, [0.5, 0.5], [0.33, 0.056])

elements = []

for button in buttons:
    elements.append(button)
elements.append(title_text)

title = Screen(elements, TITLE, LIGHT_SLATE_GREY)



# def run(screen):
#     s_w = screen.get_width()
#     s_h = screen.get_height()
#     screen.fill(LIGHT_SLATE_GREY)
#
#     title_text.draw()
#
#     for button in buttons:
#         button.draw()
#     return True
