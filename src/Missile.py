import pygame


class Missile:
    def __init__(self, screen: pygame.Surface, x, y, color="red", width=4,
                 height=8, speed=5):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.speed = speed
        self.is_off_the_screen = False
        self.has_exploded = False

    def draw(self):
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y),
                         (self.x, self.y + self.height), self.width)

    def move(self):
        self.y = self.y - self.speed
        if self.y + self.height <= 0:
            self.is_off_the_screen = True

    def explode(self):
        self.has_exploded = True
