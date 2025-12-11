import pygame

dinosaurPath = "./assets/image/dinosaur"

class Dinosaur:
    def __init__(self):
        self.__default_yPos = 425

        self.__xPos = 100
        self.__yPos = self.__default_yPos
        
        self.__dino_run = [
            pygame.image.load(dinosaurPath + "/left_run.png"),
            pygame.image.load(dinosaurPath + "/right_run.png")
        ]
        
        self.__dino_duck = [
            pygame.image.load(dinosaurPath + "/left_duck.png"),
            pygame.image.load(dinosaurPath + "/right_duck.png")
        ]
        
        self.__dino_jump = pygame.image.load(dinosaurPath + "/jump.png")
        
        self.__isRunning = True
        self.__isJumping = False
        self.__isDucking = False

        self.__run_height = self.__dino_run[0].get_height()
        self.__duck_height = self.__dino_duck[0].get_height()

        self.__gravity = -20
        
    def moveListen(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    if not self.__isJumping and not self.__isDucking:
                        self.__isRunning = False
                        self.__isDucking = True
                        diff = self.__run_height - self.__duck_height
                        self.__yPos += diff

                    if self.__isJumping:
                        self.__gravity += 10

                if event.key == pygame.K_UP:
                    if not self.__isJumping:
                        if self.__isDucking:
                            diff = self.__run_height - self.__duck_height
                            self.__yPos -= diff
                        
                        self.__isDucking = False
                        self.__isRunning = False
                        self.__isJumping = True
                        self.__gravity = -20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN and self.__isDucking:
                    self.__isDucking = False
                    self.__isRunning = True
                    diff = self.__run_height - self.__duck_height
                    self.__yPos -= diff

        if self.__isJumping:
            self.__yPos += self.__gravity
            self.__gravity += 1

            if self.__yPos >= self.__default_yPos:
                self.__yPos = self.__default_yPos
                self.__isJumping = False
                self.__isRunning = True

            return [self.__dino_jump, self.__dino_jump]

        if self.__isDucking:
            return self.__dino_duck

        return self.__dino_run
    
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
