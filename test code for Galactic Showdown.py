WIDTH = 1000
HEIGHT = 700
#Game Ideas: power up that clears entire screen
#ask how to prevent spamming when shooting
#make a power up that increases the amount of bullets you can shoot
import random
import time
gameState = ''
lives = 3
score = 0
speed = 20
allowAmmo = False
allowHeart = False
ammoAmount = 2
leaderboard = open ("leaderboard.txt", "r")
#all sounds are from http://www.orangefreesounds.com/category/music/

#timer
endCount = 5
delayTime = 1
futureTime = 5
counter = 0
counterPowerup = 0
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
ship = Actor('spaceship1')
ship.pos = (500,500)


#enemy lazer
Elazer = Actor("elazer")

#draw lazer
lazer = Actor('lazer')

#draw heart power up
heart = Actor('heart')

#draw ammo power up
ammo = Actor ('ammo')

#a list of lazer - so we can shoot multiple lazers at once
lazers = []

# a list for the viruses
viruses = []
for i in range(3):
    viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
#a list for enemy lazers
Elazers = []

#list for heart power up
hearts = []
#list for ammo power up
ammos = []

#creates the start screen image
startScreen = Actor("mainscreen")
startScreen.pos = (WIDTH/2, HEIGHT/2)

#create a background image for the game
background = Actor("background")
background.pos = (WIDTH/2, HEIGHT/2)

#creates the end screen page
endscreen = Actor("endscreen")
endscreen.pos = (WIDTH/2, HEIGHT/2)

#rules screen
rulescreen = Actor("rules")
rulescreen.pos = (WIDTH/2, HEIGHT/2)

#scoreboard
scoreboard = Actor("scoreboard")
scoreboard.pos = (WIDTH/2, HEIGHT/2)

#character screen
characterscreen = Actor("characterscreen")
characterscreen.pos = (WIDTH/2, HEIGHT/2)

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

#exit button from rules screen
button9Draw = [880, 590, 85, 70]
button9Rect = Rect(button9Draw) 
button9Value = False  
button9Color = 'green'


#Vigilante button
button5Draw = [50, 200, 180, 200]
button5Rect = Rect(button5Draw) 
button5Value = False  
button5Color = 'green'

#Imperial button
button6Draw = [250, 400, 180, 200]
button6Rect = Rect(button6Draw) 
button6Value = False  
button6Color = 'green'

#Archna button
button7Draw = [500, 200, 180, 220]
button7Rect = Rect(button7Draw) 
button7Value = False  
button7Color = 'green'

#Sagittarius button
button8Draw = [700, 370, 200, 200]
button8Rect = Rect(button8Draw) 
button8Value = False  
button8Color = 'green'



def startUp():
    '''Run this to get the program ready to run'''
    global gameState
    
    gameState = 'start screen'
    if gameState =='start screen':
        music.set_volume(0.5)
        music.play("backgroundmusic")

def on_key_down(key):
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown, ammoAmount
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
            if len(lazers) < ammoAmount: #you can only have 5 lazers at once on the screen
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
    global gameState, lives, score, speed, endCount, delayTime, futureTime, counter, gameTime, gameState
    global virusRight, virusLeft, virusStart, Elazers, lazers, viruses, moveLeft, moveRight, moveDown, moveUp, moveTopLeft
    global moveTopRight, moveBottomLeft, moveBottomRight, lazer, allowAmmo, ammoAmount, allowHeart, hearts, ammos, counterPowerup
    import random
    global button1Value, button2Value, button3Value, button4Value, button5Value, button6Value, button7Value, button8Value, button9Value

    
    if gameState == 'start screen': #to make sure buttons don't overlap
        if button1Rect.collidepoint(pos):
            '''Start game button and rules button. turns out I can't have two gameState == 'startScreen's in one
            function so I put the both together here'''

            #play game button
            gameState = 'characterscreen'
            button1Value = not button1Value
            music.play_once('buttonclicked')
                
        elif button4Rect.collidepoint(pos):
            #rules button
            gameState = 'rules'
            button4Value = not button4Value
            music.play_once('buttonclicked')

                
    elif gameState == 'characterscreen': #the ship selection screen
        if button5Rect.collidepoint(pos):
            '''this will take the user to select a ship'''

            # button
            button5Value = not button5Value
            ship.image = "spaceship2"
            gameState = 'game'
            music.play_once('buttonclicked')
              
        elif button6Rect.collidepoint(pos):
        # button
            button6Value = not button6Value
            ship.image = "spaceship3"
            gameState = 'game'
            music.play_once('buttonclicked')

                
        elif button7Rect.collidepoint(pos):
            #orange ship
            button7Value = not button7Value
            ship.image = "spaceship4"
            gameState = 'game'
            music.play_once('buttonclicked')


                
        elif button8Rect.collidepoint(pos):
            #purple ship
            button8Value = not button8Value
            ship.image = "spaceship1"
            gameState = 'game'
            music.play_once('buttonclicked')

                
    elif gameState == "end":
         #PLay again button
        if button2Rect.collidepoint(pos):
            button2Value = not button2Value
            button2Value = True
            music.play_once('buttonclicked')
            gameState = "start screen"
            lives = 3
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
            hearts = []
            ammos = []
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
            ammoAmount = 2
            counterPowerup = 0
            allowAmmo = False
            allowHeart = False
                
        if button3Rect.collidepoint(pos):
            #leaderboard button
            if button3Rect.collidepoint(pos):
                button3Value = not button3Value
                gameState = 'leaderboard'
                music.play_once('buttonclicked')

                
    elif button9Rect.collidepoint(pos):
        #exit button
        if button9Rect.collidepoint(pos):
            button9Value = not button9Value
            gameState = 'start screen'
            music.play_once('buttonclicked')
            lives = 3
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
            hearts = []
            ammos = []
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
            ammoAmount = 2
            counterPowerup = 0
            allowAmmo = False
            allowHeart = False
                
    
def update():
    global gameState, ship, moveLeft, moveRight, moveUp, moveDown, speed, lazer, lazers, virus, viruses, virusLeft, virusRight
    global score, spawn, counter, endCount, delayTime, futureTime, Elazer, Elazers, lives, gameTime, virusStart, ammo, hearts, ammos
    global allowAmmo, counterPowerup, allowHeart, ammoAmount
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
            
        if ship.x < 0: #Note for future: don't keep the y and x in the same if statements
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
                
        for ammo in ammos:
            if ammo.y > 700:
                ammos.remove(ammo)
            else:
                ammo.y += 5
                
        for heart in hearts:
            if heart.y > 700:
                hearts.remove(heart)
            else:
                heart.y += 5
                
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
                    music.set_volume(0.2)
                    music.play_once("enemy hit")
                    viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200)))) # new virus every time one is killed
                    if score > 1000 and score < 2000:
                        if len(viruses) < 4: # makes sure there can only be a maximun of 4 viruses at once
                            viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                    elif score > 2000 and score < 3000:
                        if len(viruses) < 5: # makes sure there can only be a maximun of 5 viruses at once
                            viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                    elif score > 3000 and score < 4000:
                        if len(viruses) < 6: # makes sure there can only be a maximun of 6 viruses at once
                            viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                    elif score > 5000:
                        if len(viruses) < 8: # makes sure there can only be a maximun of 8 viruses at once
                            viruses.append(Actor('virus', (random.randint(200,800), random.randint(0,200))))
                            
                else:
                    gameState == "error"
                    
            #detect collision with enemy lazer and ship      
            for Elazer in Elazers:
                if ship.colliderect(Elazer):
                    lives -= 1
                    Elazers.remove(Elazer)
                    music.set_volume(0.2)
                    music.play_once("ship hit")
                    if lives < 1:
                        music.play_once("gameover sound")
                        leaderboard = open ("leaderboard.txt", "a")
                        leaderboard.write("\r\n")
                        leaderboard.write(str(score))
                        leaderboard.close()
                        gameState = "end"
                        
       
                    
        #use a break, otherwise you'll be removing an element from the lists, thus when the lazers collide you'll
        #get an error since the lazer or elazer is no longer in the list
        for lazer in lazers:
            for Elazer in Elazers:
                if Elazer.colliderect(lazer):
                    lazers.remove(lazer)
                    Elazers.remove(Elazer)
                    break
        
        if lives < 5:#makes sure that lives cannot pass 5
            for heart in hearts:
                if ship.colliderect(heart):
                    lives += 1
                    hearts.remove(heart)
                    #music.set_volume(0.2)
                    #music.play_once("powerup")
        
        if ammoAmount < 5:
            for ammo in ammos:
                if ship.colliderect(ammo):
                    ammoAmount += 1
                    ammos.remove(ammo)
                
                
                    
        #a time for the game
        if futureTime < time.time():
            if counter < endCount:
                counter += 1;
                counterPowerup += 1
                gameTime += 1
                futureTime = time.time() + delayTime
                
            else:
                if counter == 5:
                    counter = 0
                if counterPowerup == 30:
                    counterPowerup = 0
        for virus in viruses: #took a while but this makes every virus in the list "viruses" shoot and not just one
            if counter == 5:
                Elazers.append(Actor('elazer'))
                Elazers[-1].x = virus.x
                Elazers[-1].y = virus.y
                music.set_volume(0.2)
                music.play_once("elazer sound")
        
        if ammoAmount <5:
            if counterPowerup % 30 == 0 and allowAmmo:
                ammos.append(Actor('ammo', (random.randint(100,900), 100)))
                allowAmmo = False
            if counterPowerup % 30 != 0:
                allowAmmo = True
           
        if lives < 5:
            if counterPowerup % 20 == 0 and allowHeart:
                hearts.append(Actor('heart', (random.randint(100,900), 100)))
                allowHeart = False
            if counterPowerup % 20 != 0:
                allowHeart = True
            

def draw():
    #Draws everything in each game State
    global gameState,shipX,shipY, lazer, lazers, virus, viruses, Elazer, Elazers, gameTime, endscreen, rulescreen, ammo, ammos, ammoAmount
    global scoreList
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
        #draw ammo power ups
        if ammoAmount <5:
            for ammo in ammos: #cant have more than 5 shots
                ammo.draw()
        
        #heart powerups
        if lives <5: #no more heart power ups if the user has 5(max)
            for heart in hearts:
                heart.draw()
            
    elif gameState == 'rules':
        rulescreen.draw()

        
    elif gameState == 'characterscreen':
        characterscreen.draw()
        
    elif gameState == 'leaderboard':
        scoreboard.draw()
        leaderboard = open ("leaderboard.txt", "r")
        scoreList = leaderboard.readline()
        leaderboard.close()
        screen.draw.text ("Your Score:" + str((score)), center=(WIDTH/2, 200), color="purple", fontsize = 110)
        screen.draw.text (str((scoreList)), center=(WIDTH/2, 300), color="purple", fontsize = 110)
        screen.draw.text (str((scoreList)), center=(WIDTH/2, 400), color="purple", fontsize = 110)
    
    elif gameState == 'end':
        endscreen.draw()
        screen.draw.text (str((gameTime)), center=(800, 315), color="purple", fontsize = 110)
        screen.draw.text (str((score)), center=(800, 420), color="beige", fontsize = 110)
        
    elif gameState == "error": #just to let me know if the code fails somewhere
        screen.fill((255, 204, 203))
        screen.draw.text ("Something is wrong", center=(WIDTH/2, HEIGHT/2), color="red")
        
        
startUp()