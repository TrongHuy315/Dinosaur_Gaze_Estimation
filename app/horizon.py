import pygame

horizonPath = "./assets/image/horizon"

class Horizon:
    def __init__(self):
        self.__xPos = 0
        self.__yPos = 500
        
        self.__horizon = pygame.image.load(horizonPath + "/line.png")
        
    def getHorizon(self):
        return self.__horizon
    
    def getXPos(self):
        return self.__xPos
    
    def getYPos(self):
        return self.__yPos
    
    def getHorizonWidth(self):
        return self.__horizon.get_width()
