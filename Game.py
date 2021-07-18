import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Get the RockSteady')
enemyX = []
enemyY = []
enemyimg = []
enemyXchange = []
enemyYchange = []
n = 6
heroimg = pygame.image.load('superhero.png')
enemyimg1 = pygame.image.load('rocksteady.png')
gameover = pygame.image.load('game-over.jpg')
background = pygame.image.load('background.jpg')
shield = pygame.image.load('shield.jpg')
pygame.display.set_icon(heroimg)

playerX = 450
playerY = 480
playerX_change = 0
playerY_change = 0
for i in range(n):
    enemyX.append(random.randint(0, 1000))
    enemyY.append(random.randint(64, 250))
    enemyimg.append(enemyimg1)
    enemyXchange.append(0.4)
    enemyYchange.append(40)
shieldX = 0
shieldY = 480
shieldY_change = 0.5
shield_state = "ready"
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 64)
def finscore(x, y):
    finscore = font.render('Score: ' + str(score), True, (0, 255, 0))
    screen.blit(finscore,(x, y))
def gameover(x, y):
    gameover = font2.render('GAME OVER',True,(255, 0, 0))
    screen.blit(gameover,(x,y))
def player(X, Y):
    screen.blit(heroimg, (X, Y))


def enemy(X, Y, i):
    screen.blit(enemyimg[i], (X, Y))


def go(a, b):
    screen.blit(gameover, (a, b))


def fire(x, y):
    global shield_state
    shield_state = 'fire'
    screen.blit(shield, (x + 16, y + 10))


running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            elif event.key == pygame.K_SPACE:
                if shield_state == 'ready':
                    shieldX = playerX
                    fire(shieldX, shieldY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    if playerY <= 0:
        playerY = 0
    elif playerY >= 624:
        playerY = 624

    for i in range(n):
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyXchange[i] = 0.5
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 936:
            enemyX[i] = 936
            enemyXchange[i] = -0.5
            enemyY[i] += enemyYchange[i]
        if ((((enemyX[i]) - shieldX) ** 2) + ((enemyY[i]) - shieldY) ** 2) ** (0.5) < 25:
            shieldY = 480
            shield_state = 'ready'
            score += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(64, 150)
        if enemyY[i] >= 450 and 320 <=enemyX[i] <= 390:
            for j in range(n):
                enemyY[j] = 1000
            gameover(200, 150)
            break
        enemy(enemyX[i], enemyY[i], i)
    if playerY <= 0:
        playerY = 0
    elif playerY >= 624:
        playerY = 624
    if shield_state == 'fire':
        fire(shieldX, shieldY)
        shieldY -= shieldY_change
        if shieldY == 0:
            shieldY = 480
            shield_state = 'ready'

    player(playerX, playerY)
    finscore(10, 10)
    pygame.display.update()
