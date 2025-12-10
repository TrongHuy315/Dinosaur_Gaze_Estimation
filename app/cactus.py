import pygame
import random

cactusPath = "./assets/image/cactus"

class Cactus:
    def __init__(self, speed=5):
        self.width  = 50
        self.height = 60

        self.__xPos = 1280   
        self.__yPos = 420   
        self.speed = speed

        img_big   = pygame.image.load(cactusPath + "/1_cactus.png")
        img_triple = pygame.image.load(cactusPath + "/3_cactus.png")

        self.images = [
            pygame.transform.scale(img_big, (self.width, self.height)),
            pygame.transform.scale(img_triple, (self.width, self.height))
        ]

        self.image = random.choice(self.images)

    def getXPos(self):
        return self.__xPos

    def setXPos(self, x):
        self.__xPos = x

    def getYPos(self):
        return self.__yPos

    def setYPos(self, y):
        self.__yPos = y

    def getImage(self):
        return self.image
