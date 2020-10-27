WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen

gameScreen = ''
lives = 5
score = 0
shipX = 500
shipY = 550
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

#learn to shrink the size of images/actors

#draw background
#resize background***
#background = Actor("background")
#background.pos = (500,300)

#draw ship
ship = Actor("spaceship1")
ship.pos = (500,500)



#draw virus
virus = Actor("virus")
virus.pos = (500,100)


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
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown
    import random
    #moves the ship 
    if moveRight == True:
        ship.x += 5*3
    
    elif moveLeft == True:
        ship.x -= 5*3
        
    elif moveUp == True:
        ship.y -= 5*3
        
    elif moveDown == True:
        ship.y += 5*3




def draw():
    global gameState,shipX,shipY
    
    
    
    if gameState == 'game':
        #make a space background
        #background.draw()
        screen.clear()
        ship.draw()
        virus.draw()
        screen.draw.text("Score: " + str((score)), center=(100,25), color="light blue", fontsize = 50)
        screen.draw.text("Lives: " + str((lives)), center=(900,25), color="green", fontsize = 50)
        
    
startUp()
    
    
    
    