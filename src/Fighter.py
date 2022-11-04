import pygame
from Missile import Missile
from Missiles import Missiles
from Enemy import Enemy


class Fighter:
    def __init__(self, screen: pygame.Surface, missiles: Missiles, speed=5):
        self.screen = screen
        self.image = pygame.image.load("../assets/fighter.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Fighter starts centered horizontally, near the bottom of screen.
        image_at_bottom = self.screen.get_height() - self.image.get_height()
        distance_from_bottom = 5
        self.x = (self.screen.get_width() - self.image.get_width()) // 2
        self.y = image_at_bottom - distance_from_bottom

        self.missiles = missiles
        self.speed = speed
        self.fire_sound = pygame.mixer.Sound("../assets/pew.wav")
        self.explosion_sound = pygame.mixer.Sound("../assets/explosion.wav")
        self.is_exploded = False

    def draw(self):
        if not self.is_exploded:
            self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        if self.x > -self.image.get_width() / 2:
            self.x = self.x - self.speed

    def move_right(self):
        if self.x < self.screen.get_width() - self.image.get_width() / 2:
            self.x = self.x + self.speed

    def fire(self):
        new_missile = Missile(self.screen,
                              self.x + self.image.get_width() // 2, self.y)
        self.fire_sound.play()
        self.missiles.add_missile(new_missile)

    def hit_by(self, enemy: Enemy):
        fighter_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        return fighter_rect.colliderect(enemy_rect)

    def explode(self):
        self.explosion_sound.play()
        self.is_exploded = True
