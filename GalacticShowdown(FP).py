WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen
#ask how to prevent spamming when shooting
import random
import time
gameScreen = ''
lives = 5
score = 0
shipX = 500
shipY = 550
speed = 20

#timer
endCount = 5
delayTime = 1
futureTime = 5
counter = 0
print('\r\nCurrent Time - ', time.time())
futureTime - time.time() + delayTime
print(futureTime)
gameTime = 0

#spaceship movement
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
moveTopLeft = False
moveTopRight = False
moveBottomLeft = False
moveBottomRight = False

#virus movement
virusLeft = False
virusRight = False

#learn to shrink the size of images/actors

#draw background
#resize background***
#background = Actor("background")
#background.pos = (500,300)

#draw ship
ship = Actor("spaceship1")
ship.pos = (500,500)


#enemy lazer
Elazer = Actor("elazer")

#draw lazer
lazer = Actor("lazer")

#a list of lazer - so we can shoot multiple lazers at once
lazers = []

# a list for the viruses
viruses = []

#a list for enemy lazers
Elazers = []

viruses.append(Actor("virus"))
spawn = random.randint (1,2)
if spawn == 1:
    viruses[-1].x = 40
    viruses[-1].y = random.randint(1,200)
elif spawn == 2:
    viruses[-1].x = 980
    viruses[-1].y = random.randint(1,200)
        
        
        
def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    
    gameState = 'game'


def on_key_down(key):
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown
    
    #takes player key down input for the ship
    if gameState == 'game':
        if key == key.LEFT:
            moveLeft = True
            
        elif key == key.RIGHT:
            moveRight = True
            
        elif key == key.UP:
            moveUp = True
        
        elif key == key.DOWN:
            moveDown = True
            
    #moved this to on key down instead of update so the player cannot hold down the shoot button
    if key == keys.SPACE:
        lazers.append(Actor('lazer'))
        lazers[-1].x = ship.x #we use -1 to take the last element in the list
        lazers[-1].y = ship.y
        
    
        
def on_key_up(key):
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown
    #takes player key up input for the ship
    if gameState == 'game':
        if key == key.LEFT:
            moveLeft = False
            
        elif key == key.RIGHT:
            moveRight = False
        
        elif key == key.UP:
            moveUp = False
        
        elif key == key.DOWN:
            moveDown = False
    
def update():
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown, speed, lazer, lazers, virus, viruses, virusLeft, virusRight
    global score, spawn, counter, endCount, delayTime, futureTime, Elazer, Elazers, lives, gameTime
    import random
    #moves the ship 
    if moveRight == True:
        ship.x += speed
    
    elif moveLeft == True:
        ship.x -= speed
        
    elif moveUp == True:
        ship.y -= speed
        
    elif moveDown == True:
        ship.y += speed
        
    if ship.y < 450: #makes sure that the ship cannot fly to close to the viruses
        ship.y = 440
    elif ship.y >700:
        ship.y = 690
    elif ship.x < 0:
        ship.x = 10
    elif ship.x > 1000:
        ship.x = 990

    
    for lazer in lazers:
        if lazer.y < -20: #remove the lazer from list if it goes off the screen
            lazers.remove(lazer)
            
        else: #otherwise the lazer keeps moving (on screen)
            lazer.y -= 40
            
    for Elazer in Elazers:
        if Elazer.y > 700:
            Elazers.remove(Elazer)
        else:
            Elazer.y += 30
            
    #gets the virus to move side to side
    for virus in viruses:
        '''this code took way too long to figure out...'''
        if spawn == 1:
            virus.x += 15
            if virus.x > 950:
                virus.x = 10
        elif spawn == 2:
            virus.x -= 15
            if virus.x < 50:
                virus.x = 990
        '''
        if virus.x > 950:
            virusLeft = True
        elif virus.x < 50:
            virusRight = True
            
        if virus.x < 50:
            virusLeft = False
        if virus.x > 950:
            virusRight = False
            
        if virusLeft == True:
            virus.x -=20
        elif virusRight == True:
            virus.x += 20
        '''
        
        #detect collision with lazer and virus
        for lazer in lazers:
            if virus.colliderect(lazer):
                score += 100
                lazers.remove(lazer) #remove the lazer and virus after hitting
                viruses.remove(virus)
                if len(viruses) < 3:
                    viruses.append(Actor("virus"))
                    viruses.append(Actor("virus"))
                    
        #detect collision with enemy lazer and ship      
        for Elazer in Elazers:
            if ship.colliderect(Elazer):
                lives -= 1
                Elazers.remove(Elazer)
                
        '''giving an error'''       
       # for lazer in lazers:
       #     if Elazer.colliderect(lazer):
       #         lazers.remove(lazer)
       #         Elazers.remove(Elazer)
                

    if futureTime < time.time():
        if counter < endCount:
            counter += 1;
            gameTime += 1
            futureTime = time.time() + delayTime
            
        else:
            print (counter)
            if counter == 5:
                counter = 0
                print("shoot")

    if counter == 5:
        Elazers.append(Actor('elazer'))
        Elazers[-1].x = virus.x
        Elazers[-1].y = virus.y

def draw():
    global gameState,shipX,shipY, lazer, lazers, virus, viruses, Elazer, Elazers, gameTime
    
    
    
    if gameState == 'game':
        #make a space background
        #background.draw()
        screen.clear()
        ship.draw()
        screen.draw.text("Score: " + str((score)), center=(100,25), color="light blue", fontsize = 50)
        screen.draw.text("Lives: " + str((lives)), center=(900,25), color="green", fontsize = 50)
        screen.draw.text("Time: " + str((gameTime)), center=(500,25), color="yellow", fontsize = 50)
        #drawing lazers
        for lazer in lazers:
            lazer.draw()
        #drawing viruses
        for virus in viruses:
            virus.draw()
        #draw enemy lazer
        for Elazer in Elazers:
            Elazer.draw()
        
    
startUp()
    
    
    
    