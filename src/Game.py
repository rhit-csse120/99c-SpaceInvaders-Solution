import pygame
from Fighter import Fighter
from Missiles import Missiles
from Enemies import Enemies
from ScoreBoard import ScoreBoard


class Game:
    def __init__(self, screen: pygame.Surface, enemy_rows: int = 5):
        self.screen = screen
        self.sound_to_play_when_win = pygame.mixer.Sound("../assets/win.wav")
        self.sound_to_play_when_lose = pygame.mixer.Sound("../assets/lose.wav")
        self.game_over_image = pygame.image.load("../assets/gameover.png")
        self.position_for_game_over_image = (170, 200)

        # Next two lines of code list the remaining instance variables.
        # The line after that sets their values for a new game.
        self.missiles = self.fighter = self.enemies = self.score_board = None
        self.game_is_over = self.enemy_fleet_was_destroyed = None
        self.start_a_new_game(enemy_rows)

    def start_a_new_game(self, enemy_rows):
        self.missiles = Missiles(self.screen)
        self.fighter = Fighter(self.screen, self.missiles)
        self.enemies = Enemies(self.screen, enemy_rows=enemy_rows)
        self.score_board = ScoreBoard(self.screen)
        self.game_is_over = False
        self.enemy_fleet_was_destroyed = False

    def draw_game(self):
        self.fighter.draw()
        self.missiles.draw()
        self.enemies.draw()
        self.score_board.draw()
        if self.game_is_over:
            self.screen.blit(self.game_over_image,
                             self.position_for_game_over_image)

    def run_one_cycle(self):
        if not self.game_is_over:
            self.missiles.move()
            self.enemies.move()
            self.missiles.handle_explosions(self.enemies, self.score_board)
            self.handle_enemy_fleet_destroyed()
            self.handle_fighter_is_hit()

    def handle_fighter_is_hit(self):
        for enemy in self.enemies.list_of_enemies:
            if self.fighter.hit_by(enemy):
                self.fighter.explode()
                print("Player loses!")
                self.game_is_over = True
                self.sound_to_play_when_lose.play()
                return

    def handle_enemy_fleet_destroyed(self):
        if self.enemy_fleet_was_destroyed:
            self.enemy_fleet_was_destroyed = False
            channel = self.sound_to_play_when_win.play()
            while channel.get_busy():  # Wait for sound to finish.
                pygame.time.wait(50)
            pygame.time.wait(100)
            self.start_a_new_game(self.enemies.enemy_rows + 1)
        elif len(self.enemies.list_of_enemies) == 0:
            # Just set a flag for the next iteration of run_one_cycle,
            # so that any events not yet processed can be processed.
            self.enemy_fleet_was_destroyed = True
