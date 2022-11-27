import pygame
import random
import math
# i was too bored in 2020
from pygame import mixer
#initialize the pygame
pygame.init() ##
#create screen
screen = pygame.display.set_mode((600,400))

#background
bg = pygame.image.load('background.jpg')

#Title + icon
pygame.display.set_caption("Corona 2020")
icon = pygame.image.load('soap.png')
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load('player.png')
playerX = 20
playerY = 170
playerY_change = 0

#enemy
num_of_enemy = 5
enemyImage = []
enemyX= []
enemyY= []
enemyX_change= []
enemyY_change= []
for i in range(num_of_enemy):
    enemyImage.append( pygame.image.load('virus.png'))
    enemyX.append(random.randint(400,510))
    enemyY.append(random.randint(10,330))
    enemyX_change.append(30)
    enemyY_change.append(0.5)

#bullet
# ready = bullet hidden
# fire = bullet fired
bulletImage = pygame.image.load('soap.png')
bulletX = 20
bulletY = 0
bulletX_change = 1
bulletY_change = 3
bullet_state = "ready"

#score
score = 0
font = pygame.font.Font('freesansbold.ttf',15)
textX = 600-80
textY = 400-20

# Game over text
over_font = pygame.font.Font('freesansbold.ttf',30)


def game_over_text():
    
    over_text = over_font.render("GAME OVER" , True , (0,0,0) )
    screen.blit(over_text, (100,200))
     
def show_score(x,y):
    scr = font.render("Score : " + str(score) , True , (0,0,0) )
    screen.blit(scr, (x, y))

def player(x,y):
    x = int(x)
    y = int(y)
    # draw image of player 
    screen.blit(playerImage, (x,y) )

def enemy(x,y,i):
    x = int(x)
    y = int(y)
    # draw image of player 
    screen.blit(enemyImage[i], (x,y) )
def fire(x,y):
    
    x = int(x)
    y = int(y)
    # draw image of player
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x+40,y-5))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt( math.pow((enemyX+5)-bulletX,2) + math.pow((enemyY+5)-bulletY,2) )
    if distance < 35:
        return True

#Game loop
running = True
while running:
    # to fill the screen with solid color screen.fill((10,10, 10)) # RGB
    # bg image
    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if kstroke is pressed
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playerY_change = -2.2
                    #print("pressed up key")
                if event.key == pygame.K_DOWN:
                    playerY_change = 2.2
                    #print("pressed down key")
                    
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    # starting point of player is saved as
                    # the starting point of bullet
                    
                    bulletY = playerY
                    fire(bulletX,bulletY)
                    #print("pressed space key")
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0 # we dont want it to move
                    #print("released key")
                    
    playerY += playerY_change
    #
    if(playerY <= 10):
        playerY = 10
    elif(playerY >= 330) :
        playerY = 330

    # enemy movement
    for i in range(num_of_enemy):
        # GAME OVER

        if enemyX[i] < 60 :
            for j in range(num_of_enemy):
                enemyX[j] = 2000
                game_over_text()
                break
            break
        
        enemyY[i] += enemyY_change[i]
    
        if(enemyY[i] <= 10):
            enemyY_change[i] = 0.5
            enemyX[i] -= enemyX_change[i]
        elif(enemyY[i] >= 330) :
            enemyY_change[i] = -0.5
            enemyX[i] -= enemyX_change[i]
        # collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision :
            #collision_sound = mixer.Sound('hurt.wav')
            #collision_sound.play()
            bulletX = 20
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(450,510)
            enemyY[i] = random.randint(10,330)
        enemy(enemyX[i],enemyY[i],i) 
    # bullet movement
    if(bulletX >=560):
        bulletX = 20
        bullet_state = "ready"
    if bullet_state == "fire" :
        fire(bulletX,bulletY)
        #bullet_sound = mixer.Sound('bullet_fired.wav')
        #bullet_sound.play()
        bulletX += bulletX_change
    
    # player drawn on top of the screen
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update() ##
