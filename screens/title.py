from classes.ui import *
from constants import *
import pygame

button_texts = ["Mothership", "Host Game", "Find Game", "Options", "How to Play", "Quit"]
title_text = Text("Mothership", MEDABOTS, WHITE, [2, 4], [1.5, 2])


buttons = Button.create_buttons(button_texts, GINGA_INTER, WHITE, WHITE, [2, 2], [3, 18])



def run(screen):
    s_w = screen.get_width()
    s_h = screen.get_height()
    screen.fill(LIGHT_SLATE_GREY)

    title_text.update()

    for button in buttons:
        button.update()
