import pygame
import sys
from Game import Game


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """
        Left/Right arrow keys move the Fighter left/right while key is pressed.
        Pressing the Space bar makes the Fighter fire (once per press).
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.game.fighter.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            self.game.fighter.move_right()

        if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
            self.game.fighter.fire()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
