import pygame
import random

cactusPath = "./assets/image/cactus"

class Cactus:
    def __init__(self, speed=5):
        base_width  = 40
        base_height = 100

        self.__xPos = 1280   
        self.__yPos = 420   
        self.speed = speed

        img_big   = pygame.image.load(cactusPath + "/1_cactus.png")
        img_double = pygame.image.load(cactusPath + "/2_cactus.png")
        img_triple = pygame.image.load(cactusPath + "/3_cactus.png")

        # make the triple cactus image twice as wide as the single cactus
        img1 = pygame.transform.scale(img_big, (base_width, base_height))
        img2 = pygame.transform.scale(img_double, (base_width * 2, base_height))
        img3 = pygame.transform.scale(img_triple, (base_width * 3, base_height))

        self.images = [img1, img2, img3]
        self.image = random.choice(self.images)

        # set width/height to match the chosen image so off-screen checks work
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
