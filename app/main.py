import pygame
from dinosaur import Dinosaur
from horizon import Horizon

SCREEN_SIZE = (1780, 720)
SPEED = 5

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Dinosaur Gaze Estimation")
clock = pygame.time.Clock()
running = True

dino = Dinosaur()
horizon = Horizon()

frame = 0
x1 = horizon.getXPos()
x2 = horizon.getHorizonWidth()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")
    # print(frame)
    
    x1 -= SPEED
    x2 -= SPEED
    
    if x2 == 0:
        x1 = horizon.getHorizonWidth()
    if x1 == 0:
        x2 = horizon.getHorizonWidth()
    
    screen.blit(horizon.getHorizon(), (x1, horizon.getYPos()))
    screen.blit(horizon.getHorizon(), (x2, horizon.getYPos()))
    
    if frame >= 20:
        frame = 0
    
    if (frame >= 10):
        img = dino.getDinoRun(1)
    else:
        img = dino.getDinoRun(0)
    
    screen.blit(img, (dino.getXPos(), dino.getYPos()))
    
    pygame.display.update()
    pygame.display.flip()
    
    clock.tick(60)
    
    frame += 1
    
pygame.quit()
