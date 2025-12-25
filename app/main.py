import pygame
import random
from dinosaur import Dinosaur
from horizon import Horizon
from bird import Bird
from cactus import Cactus
from cloud import Cloud
from collision import CollisionManager
from game_over import GameOverScreen
from scoreboard import Scoreboard 

SCREEN_SIZE = (1280, 620)
SPEED = 10

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Dinosaur Gaze Estimation")
clock = pygame.time.Clock()

dino = Dinosaur()
horizon = Horizon()
collision = CollisionManager()
game_over_screen = GameOverScreen(SCREEN_SIZE)
scoreboard = Scoreboard() 

MIN_OBJECT_DISTANCE = 350    
BIRD_CHANCE = 0.01
CACTUS_CHANCE = 0.015
CLOUD_CHANCE = 0.004
BIRD_HEIGHTS = [380, 400, 450]

birds = []
cloud = []
cactus_list = []

running = True
game_over = False 
frame = 0

x1 = horizon.getXPos()
x2 = horizon.getHorizonWidth()

def reset_game():
    global birds, cactus_list, cloud, frame, game_over, SPEED, x1, x2
    birds.clear()
    cactus_list.clear()
    cloud.clear()
    frame = 0
    game_over = False
    
    dino.isJumping = False
    dino.isDucking = False
    
    SPEED = 10
    x1 = horizon.getXPos()
    x2 = horizon.getHorizonWidth()
    
    scoreboard.reset()

def can_spawn(new_x, objects, min_dist):
    for obj in objects:
        if abs(new_x - obj.getXPos()) < min_dist:
            return False
    return True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    reset_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over_screen.is_retry_clicked(event.pos):
                    reset_game()
            
    screen.fill("white")
    # print(frame)
    
    if not game_over:
        scoreboard.update() 
        x1 -= SPEED
        x2 -= SPEED
        if x1 <= -horizon.getHorizonWidth(): x1 = horizon.getHorizonWidth()
        if x2 <= -horizon.getHorizonWidth(): x2 = horizon.getHorizonWidth()
        if x2 == 0: x1 = horizon.getHorizonWidth()
        if x1 == 0: x2 = horizon.getHorizonWidth()
            
        imgs = dino.moveListen(events)
        if (frame >= 10): dino_img = imgs[1]
        else: dino_img = imgs[0]
        
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

        for c in cloud[:]:
            c.update()
            if c.is_off_screen(): cloud.remove(c)

    screen.blit(horizon.getHorizon(), (x1, horizon.getYPos()))
    screen.blit(horizon.getHorizon(), (x2, horizon.getYPos()))
    
    for c in cloud:
        c.draw(screen)

    for c in cactus_list[:]:
        if not game_over:
            c.setXPos(c.getXPos() - c.speed)
            if c.getXPos() < -c.width: cactus_list.remove(c)
            
            if collision.pixel_collide(dino, c, dino_image=dino_img, obstacle_image=c.getImage()):
                game_over = True
                scoreboard.check_high_score() 

        screen.blit(c.getImage(), (c.getXPos(), c.getYPos()))

    for b in birds[:]:
        bird_img = b.getBirdFly(b.anim_index)
        if not game_over:
            b.setXPos(b.getXPos() - b.speed)
            b.anim_timer += 1
            if b.anim_timer >= 8:
                b.anim_timer = 0
                b.anim_index = (b.anim_index + 1) % 2
            if b.getXPos() < -b.width: birds.remove(b)

            if collision.pixel_collide(dino, b, dino_image=dino_img, obstacle_image=bird_img):
                game_over = True
                scoreboard.check_high_score() 
        
        screen.blit(b.getBirdFly(b.anim_index), (b.getXPos(), b.getYPos()))

    if (frame >= 10): img = imgs[1]
    else: img = imgs[0]
    screen.blit(img, (dino.getXPos(), dino.getYPos()))

    scoreboard.draw(screen) 

    if game_over:
        game_over_screen.draw(screen)

    pygame.display.update()
    clock.tick(60)
    
    if not game_over:
        frame += 1
        if frame >= 20: frame = 0

pygame.quit()