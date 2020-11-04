WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen
#ask how to prevent spamming when shooting
#make a power up that increases the amount of bullets you can shoot
import random
import time
gameState = ''
lives = 5
score = 0
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
virusRight = True

#to get the viruses to being moving at the very start
virusStart = True

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
for i in range(3):
    viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
#a list for enemy lazers
Elazers = []

#get the enemy to spawn on both sides of the screen
#viruses.append(Actor("virus"))
#spawn = random.randint (1,2)
#if spawn == 1:
#    viruses[-1].x = 40
#    viruses[-1].y = random.randint(1,200)
#elif spawn == 2:
#    viruses[-1].x = 980
#    viruses[-1].y = random.randint(1,200)
        
#creates the start screen image
startScreen = Actor("mainscreen")
startScreen.pos = (WIDTH/2, HEIGHT/2)

#create a background image for the game
background = Actor("background")
background.pos = (WIDTH/2, HEIGHT/2)

#creates the end screen page
endscreen = Actor("endscreen")
endscreen.post = (WIDTH/2, HEIGHT/2)

#rules screen
rulescreen = Actor("rules")
rulescreen.post = (WIDTH/2, HEIGHT/2)

#start button
button1Draw = [290, 380, 420, 120]
button1Rect = Rect(button1Draw) 
button1Value = False  
button1Color = 'green'

#Play Again button
button2Draw = [60, 490, 420, 90]
button2Rect = Rect(button2Draw) 
button2Value = False  
button2Color = 'green'

#leaderboard button
button3Draw = [540, 490, 420, 90]
button3Rect = Rect(button3Draw) 
button3Value = False  
button3Color = 'green'

#rules button
button4Draw = [300, 550, 400, 65]
button4Rect = Rect(button4Draw) 
button4Value = False  
button4Color = 'green'
        
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
                music.play_once("lazer sound")
        
    
        
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
    global gameState, lives, score, shipX, shipY, speed, endCount, delayTime, futureTime, counter, gameTime, gameState
    global virusRight, virusLeft, virusStart, Elazers, lazers, viruses
    import random
    global button1Color
    global button1Value
    global button2Value
    global button2Color
    global button3Value
    global button3Color
    global button4Value
    global button4Color
    
    if gameState == 'start screen': #to make sure buttons don't overlap
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
                
        if button4Rect.collidepoint(pos):
            #rules button
            if  button4Value == True:
                button4Color = 'light green'
                button4Value = False
                gameState = 'rules'
                #music.play_once('buttonclicked')
                
            else:
                button4Color == 'green'
                button4Value = True
                gameState = 'rules'
                #music.play_once('buttonclicked')
                
        
                
    if gameState == "end":
         #PLay again button
        if button2Rect.collidepoint(pos):
            if  button2Value == True:
                button2Color = (255, 250, 205)
                button2Value = False
                #music.play_once('buttonclicked')
                
            else:
                button2Value = True
                #music.play_once('buttonclicked')
                gameState = "start screen"
                lives = 5
                score = 0
                speed = 20
                endCount = 5
                delayTime = 1
                futureTime = 5
                counter = 0
                gameTime = 0
                virusLeft = False
                virusRight = True
                virusStart = True
                lazers = []
                viruses = []
                Elazers = []
                for i in range(3):
                    viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                moveLeft = False
                moveRight = False
                moveUp = False
                moveDown = False
                moveTopLeft = False
                moveTopRight = False
                moveBottomLeft = False
                moveBottomRight = False
                ship.pos = (500,500)
                
        
        #leaderboard button
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
    global score, spawn, counter, endCount, delayTime, futureTime, Elazer, Elazers, lives, gameTime, virusStart
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
            '''this code took way too long to figure out... little did I know you would expain it the very next day
                still worth the experince though'''
#            if virusStart == True:
#                virus.x += 20
#            for virus in viruses:
#                if virus.x > 950:
#                    virusStart = False
#                    virus.x -= 20
#                elif virus.x < 0:
#                    virus.x += 20
#                    virus.x = False
            
            if virus.x > 950:
                virusLeft = True
            elif virus.x < 50:
                virusRight = True
                
            if virus.x < 50:
                virusLeft = False
            elif virus.x > 950:
                virusRight = False
                
            if virusLeft == True:
                virus.x -=20
            elif virusRight == True:
                virus.x += 20
            
            
            #detect collision with lazer and virus
            for lazer in lazers:
                if virus.colliderect(lazer):
                    score += 100
                    lazers.remove(lazer) #remove the lazer and virus after hitting
                    viruses.remove(virus)
                    music.play_once("enemy hit")
                    if len(viruses) < 3: # makes sure there can only be a maximun of 4 viruses at once
                        viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                        viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                else:
                    gameState == "error"
                    
            #detect collision with enemy lazer and ship      
            for Elazer in Elazers:
                if ship.colliderect(Elazer):
                    lives -= 1
                    Elazers.remove(Elazer)
                    music.play_once("ship hit")
                    if lives < 1:
                        music.play_once("gameover sound")
                        gameState = "end"
                        
       
                    
            '''giving an error, basically want lazers to cancle eachother out'''       
        for lazer in lazers:
            if Elazer.colliderect(lazer):
                lazers.remove(lazer)
                Elazers.remove(Elazer)
                    
        #a time for the game
        if futureTime < time.time():
            if counter < endCount:
                counter += 1;
                gameTime += 1
                futureTime = time.time() + delayTime
                
            else:
                print (counter)
                if counter == 5:
                    counter = 0
                    print("run!")
        for virus in viruses: #took a while but this makes every virus in the list "viruses" shoot and not just one
            if counter == 5:
                Elazers.append(Actor('elazer'))
                Elazers[-1].x = virus.x
                Elazers[-1].y = virus.y
                music.play_once("elazer sound")

def draw():
    #Draws everything in each game State
    global gameState,shipX,shipY, lazer, lazers, virus, viruses, Elazer, Elazers, gameTime, endscreen, rulescreen
    
    if gameState == 'start screen':
        startScreen.draw()
        
        
    
    elif gameState == 'game':
        #make a space background
        #background.draw()
        screen.clear()
        background.draw()
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
    
    elif gameState == 'rules':
        rulescreen.draw()
            
    elif gameState == 'end':
        endscreen.draw()
        #screen.draw.filled_rect(button2Rect, button2Color)
        #screen.draw.filled_rect(button4Rect, button4Color)   
    
    elif gameState == "error": #just to let me know if the code fails somewhere
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red")
        
        
startUp()
    