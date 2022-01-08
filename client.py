import pygame

from classes.ui import Window
from constants import *
from screens import title

screen = Window.screen

game = True

clock = pygame.time.Clock()

current_screen = TITLE

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                game = False
            if event.key == pygame.K_ESCAPE:
                pygame.display.toggle_fullscreen()

    if current_screen == TITLE:
        title.run(screen)
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
