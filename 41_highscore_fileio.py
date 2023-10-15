def game():
    return 6798
Score = game()
with open("highscore.txt" )as f:
    highscoreStr = int(f.read())

if highscoreStr == '':
    with open('highscore.txt','w') as f:
        f.write(str(Score))
elif int(highscoreStr)<Score:       
    with open('highscore.txt','w') as f:
        
        f.write(str(Score))