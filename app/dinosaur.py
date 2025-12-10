import pygame

dinosaurPath = "./assets/image/dinosaur"

class Dinosaur:
    def __init__(self):
        self.__xPos = 100
        self.__yPos = 425
        
        self.__dino_run = [
            pygame.image.load(dinosaurPath + "/left_run.png"),
            pygame.image.load(dinosaurPath + "/right_run.png")
        ]
        
        self.__dino_duck = [
            pygame.image.load(dinosaurPath + "/left_duck.png"),
            pygame.image.load(dinosaurPath + "/right_duck.png")
        ]
        
        self.__dino_jump = pygame.image.load(dinosaurPath + "/jump.png")
        
    def getXPos(self):
        return self.__xPos
        
    def getYPos(self):
        return self.__yPos
        
    def setYPos(self, yPos):
        self.__yPos = yPos
        
    def getDinoRun(self, index):
        return self.__dino_run[index]
    
    def getDinoDuck(self, index):
        return self.__dino_duck[index]
    
    def getDinoJump(self):
        return self.__dino_jump
