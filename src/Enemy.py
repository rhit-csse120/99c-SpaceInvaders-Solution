import pygame
from Missile import Missile


class Enemy:
    def __init__(self, screen: pygame.Surface,
                 x=100, y=50, h_speed=5, v_speed=10):
        self.screen = screen
        self.image = pygame.image.load("../assets/badguy.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.h_speed = h_speed  # Increase speeds to make the game harder.
        self.v_speed = v_speed
        self.direction = 1
        self.original_x = x
        self.is_off_the_screen = False
        self.has_exploded = False
        self.explosion_sound = pygame.mixer.Sound("../assets/explosion.wav")

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = self.x + (self.h_speed * self.direction)
        if abs(self.x - self.original_x) > 100:
            # Reverse direction and move down
            self.direction = -self.direction
            self.y = self.y + self.v_speed
        if self.y > self.screen.get_height():
            self.is_off_the_screen = True

    def hit_by(self, missile: Missile):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        missile_rect = pygame.Rect(missile.x, missile.y, missile.width,
                                   missile.height)
        return enemy_rect.colliderect(missile_rect)

    def explode(self):
        self.explosion_sound.play()
        self.has_exploded = True
