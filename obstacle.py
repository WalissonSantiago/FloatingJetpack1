from settings import GROUND_Y
import random

class Obstacle:
    def __init__(self, x, images, speed, gap):
        self.speed = speed
        self.gap = gap

        gap_y = random.randint(200, GROUND_Y - 200)

        self.top_image = images[0]
        self.bottom_image = images[1]

        self.top_rect = self.top_image.get_rect(midbottom=(x, gap_y))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(x, gap_y + self.gap))

        self.passed = False

    def update(self):
        self.top_rect.x -= self.speed
        self.bottom_rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def is_off_screen(self):
        return self.top_rect.right < 0