import pygame
from dinosaur import Dinosaur
from horizon import Horizon
from bird import Bird
from cactus import Cactus
from cloud import Cloud
import random

SCREEN_SIZE = (1280, 620)
SPEED = 5

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Dinosaur Gaze Estimation")
clock = pygame.time.Clock()
running = True

dino = Dinosaur()
horizon = Horizon()

MIN_OBJECT_DISTANCE = 280    
BIRD_CHANCE = 0.015
CACTUS_CHANCE = 0.02
CLOUD_CHANCE = 0.005
BIRD_HEIGHTS = [380, 420, 450]

birds = []
cloud = []
cactus_list = []

def can_spawn(new_x, objects, min_dist):
    for obj in objects:
        if abs(new_x - obj.getXPos()) < min_dist:
            return False
    return True

frame = 0
x1 = horizon.getXPos()
x2 = horizon.getHorizonWidth()
while running:
    events = pygame.event.get()
    
    for event in events:
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
    imgs = dino.moveListen(events)
    right_edge = SCREEN_SIZE[0]

    if random.random() < CACTUS_CHANCE:
        if can_spawn(right_edge, cactus_list + birds, MIN_OBJECT_DISTANCE):
            c = Cactus(SPEED)
            c.setXPos(right_edge)
            c.setYPos(horizon.getYPos() - c.height + 25)
            cactus_list.append(c)

    if random.random() < BIRD_CHANCE:   
        if can_spawn(right_edge, birds + cactus_list, MIN_OBJECT_DISTANCE):
            b = Bird(SPEED)
            b.setXPos(right_edge)
            b.setYPos(random.choice(BIRD_HEIGHTS))
            birds.append(b)

    if random.random() < CLOUD_CHANCE:
        cloud.append(Cloud())

    for c in cactus_list[:]:
        c.setXPos(c.getXPos() - c.speed)
        screen.blit(c.getImage(), (c.getXPos(), c.getYPos()))
        if c.getXPos() < -c.width:
            cactus_list.remove(c)

    for b in birds[:]:
        b.setXPos(b.getXPos() - b.speed)
        b.anim_timer += 1
        if b.anim_timer >= 8:
            b.anim_timer = 0
            b.anim_index = (b.anim_index + 1) % 2
        screen.blit(b.getBirdFly(b.anim_index), (b.getXPos(), b.getYPos()))
        if b.getXPos() < -b.width:
            birds.remove(b)

    for c in cloud[:]:
        c.update()
        c.draw(screen)
        if c.is_off_screen():
            cloud.remove(c)


    if frame >= 20:
        frame = 0
    
    if (frame >= 10):
        img = imgs[1]
    else:
        img = imgs[0]
    
    screen.blit(img, (dino.getXPos(), dino.getYPos()))
    
    pygame.display.update()
    pygame.display.flip()
    
    clock.tick(60)
    
    frame += 1
    

    
pygame.quit()
