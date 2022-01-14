import pygame

from classes.ui import Window
from constants import *
from screens import title

window = Window.screen

game = True

clock = pygame.time.Clock()

current_screen = TITLE
title =

cs = None

while game:
    Window.update(c_s.elements)
    if current_screen == TITLE:
        title.run()
    elif current_screen == HOST:
        pass
    elif current_screen == FIND:
        pass
    elif current_screen == HOW2PLAY:
        pass
    elif current_screen == OPTIONS:
        pass
    elif current_screen == LOBBY:
        pass
    elif current_screen == GAME:
        pass

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
