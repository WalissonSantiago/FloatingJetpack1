import pygame as pg

from settings import GRAVITY, JETPACK_FORCE, HEIGHT


class Player:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(center=(150, HEIGHT // 2))
        self.velocity_y = 0

    def update(self, keys):
        if keys[pg.K_SPACE]:
            self.velocity_y = -JETPACK_FORCE

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)