from math import sqrt, cos, sin
import pygame
from classes.screen import Window

class Mothership:
    def __init__(self, color, start_pos):
        self.color = color
        self.center_ratio = start_pos
        self.size_ratio = [0.1, 0.1]
        self.rect = pygame.Rect(self.get_pos(), self.get_size())

    def tick(self):
        pass

    def draw(self):
        pass

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        x_r, y_r = self.center_ratio
        return s_w * x_r, s_h * y_r

    def get_size(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        w_r, h_r = self.size_ratio
        return [s_w * w_r, s_h * h_r]

    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            elif event.key == pygame.K_a:
                pass
            elif event.key == pygame.K_s:
                pass
            if event.key