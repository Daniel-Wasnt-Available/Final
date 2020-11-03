WIDTH = 1000
HEIGHT = 700
gameScreen = ''
gameState = 'end'
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
#creates the end screen page
endscreen = Actor("endscreen")
endscreen.post = (WIDTH/2, HEIGHT/2)
#exit button
exitsign = Actor("exit")
exitsign.pos = (400, 400)
def on_mouse_up(pos, button):
    global button2Value
    global button2Color
    
    if gameState == "end":
         #PLay again button
        if button2Rect.collidepoint(pos):
            if  button2Value == True:
                button2Color = (255, 250, 205)
                button2Value = False
                gameState = 'rules'
                #music.play_once('buttonclicked')

            else:
                button2Value = True
                gameState = 'rules'
                #music.play_once('buttonclicked')
        
def draw():
    if gameState == 'end':
        endscreen.draw()
        exitsign.draw()
        screen.draw.filled_rect(button2Rect, button2Color)
        screen.draw.filled_rect(button3Rect, button3Color)