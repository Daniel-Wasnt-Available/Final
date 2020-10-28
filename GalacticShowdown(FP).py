WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen
#ask how to prevent spamming when shooting
import random
gameScreen = ''
lives = 5
score = 0
shipX = 500
shipY = 550
speed = 20

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

moveTopLeft = False
moveTopRight = False
moveBottomLeft = False
moveBottomRight = False

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




#draw lazer
lazer = Actor("lazer")

#a list of lazer - so we can shoot multiple lazers at once
lazers = []

# a list for the viruses
viruses = []

viruses.append(Actor("virus"))
spawn = random.randint (1,2)
if spawn == 1:
    viruses[-1].x = 40
    viruses[-1].y = random.randint(1,100)
if spawn == 2:
    viruses[-1].x = 980
    viruses[-1].y = random.randint(1,100)
        
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
    global score, spawn
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

    
    for lazer in lazers:
        if lazer.y < -20: #remove the lazer from list if it goes off the screen
            lazers.remove(lazer)
            
        else: #otherwise the lazer keeps moving (on screen)
            lazer.y -= 40
            
            
            
            
    for virus in viruses:
        '''this code took way too long to figure out...'''
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
        
        for lazer in lazers:
            if virus.colliderect(lazer):
                score += 100
                lazers.remove(lazer) #remove the lazer and virus after hitting
                viruses.remove(virus)
                viruses.append(Actor("virus"))
                





def draw():
    global gameState,shipX,shipY, lazer, lazers, virus, viruses
    
    
    
    if gameState == 'game':
        #make a space background
        #background.draw()
        screen.clear()
        
        ship.draw()
        screen.draw.text("Score: " + str((score)), center=(100,25), color="light blue", fontsize = 50)
        screen.draw.text("Lives: " + str((lives)), center=(900,25), color="green", fontsize = 50)
        #drawing lazers
        for lazer in lazers:
            lazer.draw()
        #drawing viruses
        for virus in viruses:
            virus.draw()
        
    
startUp()
    
    
    
    