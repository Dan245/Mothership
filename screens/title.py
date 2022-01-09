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
title_text = Text("Mothership", GINGA_INTER, WHITE, [2, 4], [1.5, 4])
# host_button = Button("Host Game", GINGA_INTER, WHITE, 5, WHITE, s_w/2, button_y[0], button_size)
# find_button = Button("Find Game", GINGA_INTER, WHITE, 5, WHITE, s_w/2, button_y[1], button_size)
# options_button = Button("Options", GINGA_INTER, WHITE, 5, WHITE, s_w/2, button_y[2], button_size)
# tutorial_button = Button("How to Play", GINGA_INTER, WHITE, 5, WHITE, s_w/2, button_y[3], button_size)
# quit_button = Button("Quit", GINGA_INTER, WHITE, 5, WHITE, s_w/2, button_y[4], button_size)
#
# buttons = pygame.sprite.Group()
# buttons.add(host_button)
# buttons.add(find_button)
# buttons.add(options_button)
# buttons.add(tutorial_button)
# buttons.add(quit_button)

def run(screen):
    s_w = screen.get_width()
    s_h = screen.get_height()
    screen.fill(LIGHT_SLATE_GREY)

    title_text.update()

    # buttons.draw(screen)
    # for button in buttons:
    #     button.text.display(button.rect.center[0], button.rect.center[1])
