import pygame
import random

cloudPath = "./assets/image/cloud"

class Cloud:
    def __init__(self):
        self.img = pygame.image.load(cloudPath + "/cloud.png")
        self.img = pygame.transform.scale(self.img, (90, 40))

        self.x = 1280
        self.y = random.randint(80, 200)

        self.speed = 1

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def is_off_screen(self):
        return self.x + self.img.get_width() < 0
