import pygame


class ScoreBoard:
    def __init__(self, screen: pygame.Surface, points_per_enemy=100, x=0, y=0,
                 font_class="Consolas", font_size=24,
                 font_color=pygame.Color("Black"),
                 background=pygame.Color("White")):
        self.screen = screen
        self.points_per_enemy = points_per_enemy
        self.x = x
        self.y = y
        self.font_class = font_class
        self.font_size = font_size
        self.font_color = font_color
        self.background = background

        self.font = pygame.font.SysFont(self.font_class, self.font_size)
        self.score = 0

    def draw(self):
        print("Draw score")  # Just for testing, remove later.

        caption = self.font.render(" Score: {} ".format(self.score), True,
                                   self.font_color, self.background)
        self.screen.blit(caption, (self.x, self.y))

    def increment_score(self):
        print("Increment score")  # Just for testing, remove later.
        
        self.score = self.score + self.points_per_enemy
