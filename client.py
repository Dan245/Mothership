import pygame

from constants import *
from classes.screen import Window
from screens.title import title
from screens.host import host
from screens.find import joinn

screens = [title, host, joinn]

window = Window.screen

clock = pygame.time.Clock()

game = TITLE
last_screen = game

while game:
    game = Window.update(game, screens[game-1].elements)
    if not game:
        continue
    screens[game-1].run(last_screen)
    pygame.display.flip()
    last_screen = game
    clock.tick(FPS)
pygame.quit()
