import pygame
from pygame import QUIT, Surface, Rect
import random
from models.config import config


class Game:
    def __init__(self):
        self.main_surface: Surface = pygame.display.set_mode(config.screen)
        self.ball: Surface = pygame.Surface(config.ball_size)
        self.ball_rect: Rect = self.ball.get_rect()
        self.velocity = config.velocity
        self.initialize_game()

    def initialize_game(self):
        self.ball.fill((255, 255, 255))
        is_working: bool = True
        while is_working:
            for event in pygame.event.get():
                if event.type == QUIT:
                    is_working = False

            self.ball_rect = self.ball_rect.move(self.velocity)
            self.check_collision()
            self.main_surface.fill((0, 0, 0))
            self.main_surface.blit(self.ball, self.ball_rect)

            pygame.display.flip()

    def check_collision(self) -> None:
        if self.ball_rect.bottom >= config.screen[1] or self.ball_rect.top <= 0:
            config.velocity[1] = -config.velocity[1]
            self.change_ball_color()
        if self.ball_rect.right >= config.screen[0] or self.ball_rect.left <= 0:
            config.velocity[0] = -config.velocity[0]
            self.change_ball_color()

    def change_ball_color(self):
        self.ball.fill((random.sample(range(255), 3)))


if __name__ == "__main__":
    Game()
