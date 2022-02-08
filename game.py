#Imports game library that let's you use specific
#functions for your program
import pygame

#Import to generate random numbers
import random

#Initialize pygame modules
pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1700
screen_height = 800

# This creates the screen 
# and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width,screen_height))

#This creates the player and enemy with images inside the folder
#Also making two extra enemies and a prize
player = pygame.image.load("player.jpg")
enemy = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

#Now for the wigth and height for the enemies, player and prize
#for boundary detection
player_height = player.get_height()
player_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_widht = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

#Now for the position of the player
playerXPosition = 100
playerYPosition = 50

#Now the position for the prize
prizeXPosition = 500
prizeYPosition = 500

#Now to make the enemy start off screen on a random y position
enemyXPosition =  screen_width
enemyYPosition =  0
enemy2XPosition =  screen_width
enemy2YPosition =  250
enemy3XPosition =  screen_width
enemy3YPosition =  500

#Now to check if the up, down, left or right key is pressed
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

while 1:

    screen.fill(0) #This cleares the screen
    screen.blit(player, (playerXPosition, playerYPosition))

    screen.blit(enemy, (enemyXPosition, enemyYPosition))

    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))

    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    screen.blit(prize, (prizeXPosition, prizeYPosition))

    #This updates the screen
    pygame.display.flip()

    #This loops through the events of the game
    for event in pygame.event.get():

        #The following if statement checks if the users quites the game
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)

        #This if statement checks if the user pressed the donw key
        if event.type == pygame.KEYDOWN:

            #Test if the key pressed is the one we want in all directions.
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        #This if statement is to check if the key is up
        if event.type == pygame.KEYUP:

            #To test if the release is the one we want
            if event.type == pygame.K_UP:
                keyUp = False
            if event.type == pygame.K_DOWN:
                keyDown = False
            if event.type == pygame.K_LEFT:
                keyLeft = False
            if event.type == pygame.K_RIGHT:
                keyRight = False

    #Now to work on the movement of the player with the coordinate system
    #Up direction
    if keyUp == True:
        if playerYPosition > 0: #This makes sure the player does not move past the window
            playerYPosition -= 1

    #Down direction
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1

    #Left direction
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1

    #Right direction
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    #Now to check for the collision
    #with player, enemy and prize
    #First the player box

    playerBox = pygame.Rect(player.get_rect())

    #Now for the box update as the player moves
    #So the box stayes around the player
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition


    #Now the boxes for the enemies
    enemyBox = pygame.Rect(enemy.get_rect())

    #Now to update the boxes of each object
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition


    #Second enemy box
    enemy2Box = pygame.Rect(enemy.get_rect())

    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition


    #Thrid enemy box
    enemy3Box = pygame.Rect(enemy.get_rect())

    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    

    #Now to create the box for the prize
    prizeBox = pygame.Rect(prize.get_rect())

    #Now I update the position of the box for the prize
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    #Now the collition for the boxes
    if playerBox.colliderect(enemyBox):

        #If the statement is True, the following print
        #statement will be triggerd
        print("You lose!")
        
        #When the print function is triggerd the game automatically quits
        pygame.quit
        exit(0)

    #Now the elif statement for the other enemies
    elif playerBox.colliderect(enemy2Box):

        print("You lose!")
        pygame.quit
        exit(0)

    elif playerBox.colliderect(enemy3Box):
        
        print("You lose!")
        pygame.quit
        exit(0)

    #Now to make the if statement to make the player win
    if playerBox.colliderect(prizeBox):

        print("You win!")

        #Quit the game
        pygame.quit

        exit(0)

    #To make the all enemies approach 
    #approach the player at once
    enemyXPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15
 


            

        
        

