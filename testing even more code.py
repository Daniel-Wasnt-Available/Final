WIDTH = 1000
HEIGHT = 700
score=100


leaderboard = open("leaderboard.txt")
lines = [0, 2]

for line, line in enumerate(leaderboard):

    if line == 1:
        print(line)
        
def draw():
    screen.draw.text (str((line)), center=(WIDTH/2, 300), color="purple", fontsize = 110)