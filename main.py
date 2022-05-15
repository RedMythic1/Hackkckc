##Team Members: Udayan, Dhariya, Avneh, Arushthecow
import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
starter_weapon = 5
player_health = 25
player_defense = 0
pygame.display.set_caption("Trash Attack")
icon = pygame.image.load('bottle.png')
trash = pygame.transform.scale(icon, (75, 75))
trashX = 350
trashY = 0
playerImg = pygame.image.load("char.png")
playerImg = pygame.transform.scale(playerImg, (100, 100))
playerX_change = 0
playerX = 0
playerY = 456
enemyImg = pygame.image.load("bottle.png")
enemyImg = pygame.transform.scale(enemyImg, (20, 20))
enemyX_change = 0
enemyX = 0
enemyY = 0
grassImg = pygame.image.load("grass.png")
grassImg = pygame.transform.scale(grassImg, (800, 200))
grassX = 0
grassY = 400
global score
score = 0
current_weapon = 'fist'




def grass():
    screen.blit(grassImg, (grassX, grassY))


def player():
    screen.blit(playerImg, (playerX, playerY))


def enemy():
    screen.blit(enemyImg, (enemyX, enemyY))


running = True
while running:
    screen.fill((135, 206, 234))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        grass()
        player()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
        grass()
        player()
        pygame.display.update()
        if trashY>=550:
          print("you have lost")
          running==False
    for loop in range(100):
        trashY += .01
        screen.blit(trash, (trashX, trashY))
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
      if playerX-50<trashX<playerX+50 and playerY-50<trashY<playerY+50:
        score += 1
        print('You have collected the trash.')
        print(f"{score}")
        trashX=random.randint(playerX+50, 300)
        trashY=random.randint(0,250)
        screen.blit(trash, (trashX, trashY))
if score == 5:
    current_weapon = 'picker'
elif score == 10:
    current_weapon = 'claw'
elif score == 20:
    current_weapon = 'truck'
if current_weapon == 'fist':
    score = score + 1
elif current_weapon == 'picker':
    score = score + 5
elif current_weapon == 'claw':
    score = score + 10
elif current_weapon == 'truck':
    score = score + 20
if score == 200:
    print("You have achieved fast collector!")
if score == 500:
    print("You have achieved greatest collector!")
if score == 1000:
    print("You have achieved master collector!")

    grass()
    player()
    enemy()
    pygame.display.update()
