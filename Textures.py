import pygame
from random import randint
import numpy as np
m = randint(3, 5)
n = randint(3, 5)
l = randint(3, 6)
k = randint(3, 6)
o = randint(5, 7)
p = randint(5, 8)
r = randint(3, 6)
s = randint(3, 6)
t = randint(3, 5)


abv = [[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
       ],
       [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
       ],
       [[1,1,1,1,1,m,1,3,4,5,6,1,9,1,1,1,1,m,1,1,1,1,t,1,l,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,s,1,1,1,1,1,m,9,9,1,1,1,r,1,9,9,9,1,1,1,k,1,1,k,1,0,1],
        [1,0,9,1,s,1,1,n,1,1,1,1,1,9,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,m,1,1,1,1,1,r,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,l],
        [0,0,1,1,1,1,1,1,9,0,0,0,0,0,0,0,9,1,1,k,1,1,1,8,m,n,1,1,1,1],
        [1,1,1,1,1,1,1,k,1,0,l,9,1,1,1,1,k,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,o,1,p,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,9,1,1,n,l,1,1],
        [1,1,1,1,1,m,1,1,1,0,9,1,1,m,1,1,1,1,1,k,1,1,l,1,1,1,1,1,1,1],
        [0,0,9,1,k,1,1,1,9,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,o,9,1,1,1,1],
        [t,0,1,9,1,n,1,1,1,1,l,1,r,1,1,0,1,1,9,1,1,1,1,1,9,1,1,1,1,1],
        [1,0,1,1,1,1,1,1,p,1,1,1,s,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,t,9,1,s,1,1,1,1,1,1,1,p,1,9,1,m,1,1,n,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,t,s,1,1,1,n,1,1,1,1,1,n,1,r,1,1,1,l,1,1,n,1,1,1,1,1,1,1]
       ]
      ]

stage = 3      

grass_surf = pygame.image.load("img/t1gr.png")
grass1_surf = pygame.image.load("img/t2gr.png")
road_surf = pygame.image.load("img/t1ro.png")
cloud_surf = pygame.image.load("img/cloud.png")
ss1_surf = pygame.image.load("img/ss1.png")
ss2_surf = pygame.image.load("img/ss2.png")
ss3_surf = pygame.image.load("img/ss3.png")
ss4_surf = pygame.image.load("img/ss4.png")
stone_surf = pygame.image.load("img/stone.png")
lake_surf = pygame.image.load("img/lake.png")
enemy1_surf = pygame.image.load("img/11.png")
enemy2_surf = pygame.image.load("img/12.png")
enemy3_surf = pygame.image.load("img/13.png")
enemy4_surf = pygame.image.load("img/14.png")
fort_surf = pygame.image.load("img/mom-tower-t.png")
dmg_surf = pygame.image.load("img/dmg.png")
prb_surf = pygame.image.load("img/prb.png")
WIDTH = 1200
HEIGHT = 800
BULLET_SPEED = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def textures():
    for a in range(15):
        for b in range(30):
            if abv[stage-1][a][b] == 1:
                i = grass_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(grass_surf, i)
            elif abv[stage-1][a][b] == 9:
                i = grass1_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(grass1_surf, i)
            elif abv[stage-1][a][b] == 0:
                i = road_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(road_surf, i)
            elif abv[stage-1][a][b] == 3:
                i = ss1_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss1_surf, i)
            elif abv[stage-1][a][b] == 4:
                i = ss2_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss2_surf, i)
            elif abv[stage-1][a][b] == 5:
                i = ss3_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss3_surf, i)
            elif abv[stage - 1][a][b] == 6:
                i = ss4_surf.get_rect(center=(20 + (b * 40), (a * 40) + 20))
                screen.blit(ss4_surf, i)
            elif abv[stage - 1][a][b] == 7:
                i = stone_surf.get_rect(center=(0 + (b * 40), (a * 40) + 0))
                screen.blit(stone_surf, i)
            elif abv[stage - 1][a][b] == 8:
                i = lake_surf.get_rect(center=(0 + (b * 40), (a * 40) + 0))
                screen.blit(lake_surf, i)


def draw_bullet(x, y):
	pygame.draw.circle(screen, BLACK, (x, y), 1)

def draw_tower(x, y, z):
    if z == 1:
        tower_surf = pygame.image.load("img/tt1.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
    if z == 2:
        tower_surf = pygame.image.load("img/tt2.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
    if z == 3:
        tower_surf = pygame.image.load("img/tt3.png")
        i = tower_surf.get_rect(center=(x, y))
        screen.blit(tower_surf, i)
def draw_tower1(x, y, z):
    tower_surf = pygame.image.load("img/tt1.png")
    i = tower_surf.get_rect(center=(x, y))
    screen.blit(tower_surf, i)

def draw_enemy(enemy, time):
    change = time - enemy.time_creation
    if enemy.tik == 0:
        enemy.tik = 4
    if change//40 == change/40:
        enemy.tik -= 1
    if enemy.tik == 4:
        i = enemy1_surf.get_rect(center=( (enemy.x), (enemy.y) ))
        screen.blit(enemy1_surf, i)
    if enemy.tik == 3:
        i = enemy2_surf.get_rect(center=(  (enemy.x), (enemy.y)  ))
        screen.blit(enemy2_surf, i)
    if enemy.tik == 2:
        i = enemy3_surf.get_rect(center=(  (enemy.x), (enemy.y)  ))
        screen.blit(enemy3_surf, i)
    if enemy.tik == 1:
        i = enemy4_surf.get_rect(center=((enemy.x), (enemy.y)))
        screen.blit(enemy4_surf, i)
    if enemy.hp < 50:
        i = dmg_surf.get_rect(center=(  (enemy.x), (enemy.y)  ))
        screen.blit(dmg_surf, i)
def draw_enemy1(enemy, time):
    change = time - enemy.time_creation
    i = prb_surf.get_rect(center=((enemy.x), (enemy.y)))
    screen.blit(prb_surf, i)
def draw_enemy3(enemy, time):
    change = time - enemy.time_creation
    i = cloud_surf.get_rect(center=((enemy.x), (enemy.y)))
    screen.blit(cloud_surf, i)


def draw_fort(fort):
    i = fort_surf.get_rect(center=((860), (290)))
    screen.blit(fort_surf, i)

