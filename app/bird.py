import pygame
birdPath = "./assets/image/bird"

class Bird:
    def __init__(self, speed=5):
        self.width  = 46
        self.height = 40

        self.__xPos = 800
        self.__yPos = 400

        self.anim_index = 0
        self.anim_timer = 0
        self.speed = speed

        img1 = pygame.image.load(birdPath + "/bird_lower.png")
        img2 = pygame.image.load(birdPath + "/bird_upper.png")

        self.__bird_fly = [
            pygame.transform.scale(img1, (self.width, self.height)),
            pygame.transform.scale(img2, (self.width, self.height))
        ]

    def getXPos(self):
        return self.__xPos

    def setXPos(self, x):
        self.__xPos = x

    def getYPos(self):
        return self.__yPos

    def setYPos(self, y):
        self.__yPos = y

    def getBirdFly(self, index):
        return self.__bird_fly[index]
