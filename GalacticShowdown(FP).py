WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen

gameScreen = ''
lives = 5
score = 0

#learn to shrink the size of images/actors

#draw background
#resize background***
background = Actor("background")
background.pos = (500,300)

#draw ship
ship = Actor("spaceship2")
shipX = 500
shipY = 600



#draw virus
virus = Actor("virus")
virus.pos = (500,100)

def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    
    gameState = 'game'

def on_key_down():
    global gameState, shipX, shipY
    
    if gameState == 'game':
        if keyboard.left:
            shipX -=8
        elif keyboard.right:
            shipY += 8

def updateShip():
    global gameState, shipX, shipY
    if gameState == 'game':
        if keyboard.left:
            shipX -=8
        elif keyboard.right:
            shipY += 8



def draw():
    global gameState
    
    #make a space background
    background.draw()
    ship.draw()
    virus.draw()
    
    
startUp()
    
    
    
    