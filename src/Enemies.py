import pygame
from Enemy import Enemy


class Enemies:
    def __init__(self, screen: pygame.Surface, enemy_rows=5, enemies_per_row=8,
                 h_space_between_enemies=10, v_space_between_enemies=10,
                 distance_from_top=20, h_speed=3, v_speed=10):
        self.screen = screen
        self.enemy_rows = enemy_rows
        self.enemies_per_row = enemies_per_row
        self.h_space_between_enemies = h_space_between_enemies
        self.v_space_between_enemies = v_space_between_enemies
        self.distance_from_top = distance_from_top
        self.h_speed = h_speed
        self.v_speed = v_speed

        throw_away_enemy = Enemy(screen)
        enemy_width = throw_away_enemy.image.get_width()
        enemy_height = throw_away_enemy.image.get_height()

        enemy_space_per_row = self.enemies_per_row * enemy_width
        in_between_space_per_row = (self.enemies_per_row - 1) \
                                   * self.h_space_between_enemies
        fleet_width = enemy_space_per_row + in_between_space_per_row
        xstart = (screen.get_width() - fleet_width) // 2
        ystart = self.distance_from_top

        self.list_of_enemies: list[Enemy] = []
        x = xstart
        y = ystart
        for k in range(self.enemy_rows):
            for j in range(self.enemies_per_row):
                self.list_of_enemies.append(Enemy(screen, x, y,
                                                  self.h_speed, self.v_speed))
                x = x + enemy_width + self.h_space_between_enemies
            x = xstart
            y = y + enemy_height + self.v_space_between_enemies

    def draw(self):
        for enemy in self.list_of_enemies:
            enemy.draw()

    def move(self):
        for k in range(len(self.list_of_enemies) - 1, -1, -1):
            self.list_of_enemies[k].move()
            if self.list_of_enemies[k].is_off_the_screen:
                del self.list_of_enemies[k]

    def remove_exploded_enemies(self):
        for k in range(len(self.list_of_enemies) - 1, -1, -1):
            missile = self.list_of_enemies[k]
            if missile.is_off_the_screen or missile.has_exploded:
                del self.list_of_enemies[k]
