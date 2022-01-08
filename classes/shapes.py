from math import sqrt, cos, sin
import pygame


class Polygon:
    def __init__(self, color, rel_points, coords, center, screen):
        self.color = color
        self.rel_points = rel_points
        self.coords = coords
        self.center = center
        self.screen = screen
        self.vel = (0, 0)

    def move(self):
        centerX, centerY = self.center
        velX, velY = self.vel
        self.center = (centerX + velX, centerY + velY)
        self.draw()

    def accel(self):
        centerX, centerY = self.center

    def rotate(self, deg):
        centerX, centerY = self.center
        for i in range(len(self.coords)):
            oldX, oldY = self.coords[i]
            newX = centerX + (oldX - centerX) * cos(deg) - (oldY - centerY) * sin(deg)
            newY = centerY + (oldX - centerX) * sin(deg) + (oldY - centerY) * cos(deg)
            self.coords[i] = (newX, newY)

    def get_distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_coords(self):
        centerX, centerY = self.center
        self.coords = []
        for i in range(len(self.rel_points)):
            self.coords.append(self.rel_points[i](centerX, centerY))

    def draw(self):
        self.get_coords()
        pygame.draw.polygon(self.screen, self.color, self.coords)


# class Mothership(Polygon):
#     def __init__(self, center)
#         super().__init__(color, 10, )
