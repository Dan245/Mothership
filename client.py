import pygame

from classes.ui import Window
from constants import *
from screens.title import *
from screens.host import *
from classes.screen import Window

window = Window.screen
game = True

clock = pygame.time.Clock()

current_screen = HOST

while game:
    game = Window.update(host.elements)
    if current_screen == TITLE:
        title.run()
    elif current_screen == HOST:
        host.run()
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
