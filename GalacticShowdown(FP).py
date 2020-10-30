WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen
#ask how to prevent spamming when shooting
#make a power up that increases the amount of bullets you can shoot
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

#get the enemy to spawn on both sides of the screen
viruses.append(Actor("virus"))
spawn = random.randint (1,2)
if spawn == 1:
    viruses[-1].x = 40
    viruses[-1].y = random.randint(1,200)
elif spawn == 2:
    viruses[-1].x = 980
    viruses[-1].y = random.randint(1,200)
        
#creates the start screen image
startScreen = Actor("mainscreen")
startScreen.pos = (WIDTH/2, HEIGHT/2)

#start button
button1Draw = [290, 380, 420, 120]
button1Rect = Rect(button1Draw) 
button1Value = False  
button1Color = 'green'
        
def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    
    gameState = 'start screen'


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
            if len(lazers) < 5: #you can only have 5 lazers at once on the screen
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
    
def on_mouse_up(pos, button):
    '''Pygame Special Event Hook - Runs when the mouse button is released'''
    global gameState
    import random
    global button1Color
    global button1Value
    global button2Value
    global button2Color
    
    if gameState == 'start screen':
        if button1Rect.collidepoint(pos):
            '''Start game button and rules button. turns out I can't have two gameState == 'startScreen's in one
            function so I put the both together here'''

            #play game button
            if  button1Value == True:
                button1Color = 'light green'
                button1Value = False
                gameState = 'game'
                #music.play_once('buttonclicked')
                
            else:
                button1Color == 'green'
                button1Value = True
                gameState = 'game'
                #music.play_once('buttonclicked')
                
        #rules button
        elif button3Rect.collidepoint(pos):
            if  button3Value == True:
                button3Color = (255, 250, 205)
                button3Value = False
                gameState = 'rules'
                #music.play_once('buttonclicked')

            else:
                button3Value = True
                gameState = 'rules'
                #music.play_once('buttonclicked')
    
def update():
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown, speed, lazer, lazers, virus, viruses, virusLeft, virusRight
    global score, spawn, counter, endCount, delayTime, futureTime, Elazer, Elazers, lives, gameTime
    import random
    #moves the ship
    if gameState == 'game':
    
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
    
    if gameState == 'start screen':
        startScreen.draw()
        
    
    elif gameState == 'game':
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
    
    
    
    