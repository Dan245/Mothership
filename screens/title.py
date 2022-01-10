from classes.ui import *
from constants import *
import pygame

# s = Window.screen
# s_w = s.get_width()
# s_h = s.get_height()
# button_y = [s_h/2,]
# for i in range(1,5):
#     button_y.append(button_y[i-1]+s_h/12)
# button_size = (s_w/3, s_h/15)
title_text = Text("Mothership", MEDABOTS, WHITE, [2, 4], [1.5, 4])
host_button = Button("Host Game", GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])
find_button = Button("Find Game", GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])
options_button = Button("Options", GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])
tutorial_button = Button("How to Play", GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])
quit_button = Button("Quit", GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])

buttons = [host_button, find_button, options_button, tutorial_button, quit_button]

def run(screen):
    s_w = screen.get_width()
    s_h = screen.get_height()
    screen.fill(LIGHT_SLATE_GREY)

    title_text.update()

    for button in buttons:
        button.update()
