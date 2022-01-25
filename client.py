import pygame

from constants import *
from classes.screen import Window
from screens.title import title
from screens.host import host
from screens.find import joinn

screens = [title, host, joinn]

window = Window.screen
game = True

clock = pygame.time.Clock()

current_screen = TITLE

while game:
    game = current_screen if Window.update(screens[current_screen-1].elements) else 0
    print(game)

    screens[current_screen-1].run()
    pygame.display.flip()
    current_screen = game
    clock.tick(FPS)
pygame.quit()
