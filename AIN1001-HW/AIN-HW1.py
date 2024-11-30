import time
import random

print("Welcome to the Lucky Dice Game")
while True:
    lucky_block1 = int(input("First lucky block1: \n"))
    lucky_block2 = int(input("Second lucky block2: \n"))
    penalty_block1 = int(input("First penalty block1: \n"))
    penalty_block2 = int(input("Second penalty block2: \n"))

    if (0<lucky_block1<100) and (0<lucky_block2<100) and (10<penalty_block1<100) and (10<penalty_block2<100):
        if not ((penalty_block1 == lucky_block1) or (penalty_block1 == lucky_block2) or (penalty_block2 == lucky_block1) or (penalty_block2 == lucky_block2)):
            if not ((penalty_block1 - lucky_block1 == 10) or (penalty_block1 - lucky_block2 == 10) or (penalty_block2 - lucky_block1 == 10) or (penalty_block2 - lucky_block2 == 10)):
                break

score1 = 0
score2 = 0
while (score1 < 100) and (score2 < 100):

    print("player1^s turn")
    player1 = random.randint(1,6)
    print("Dice rolling...")
    time.sleep(2)
    if  (score1 == penalty_block1) or (score1 == penalty_block2):
        print(player1)
        score1 -= 10 
        print("Penalty block :(")
        print("Your current score is {}\n".format(score1))

    elif (score1 == lucky_block1) or (score1 == lucky_block2):
        print(player1)
        score1 += 10
        print("Wow, you are so lucky....")
        print("Your current score is {}\n".format(score1))

    else:
        print(player1)
        score1 += player1
        print("Your current score is {}\n".format(score1))

    print("player2^s turn")
    player2 = random.randint(1,6)
    print("Dice rolling...")
    time.sleep(2)    
    if  (score2 == penalty_block1) or (score2 == penalty_block2):
        print(player2)
        score2 -= 10
        print("Penalty block :(")
        print("Your current score is {}\n".format(score2))

    elif (score2 == lucky_block1) or (score2 == lucky_block2):
        print(player2)
        score2 += 10
        print("Wow, you are so lucky....")
        print("Your current score is {}\n".format(score2))

    else:
        print(player2)
        score2 += player2  
        print("Your current score is {}\n".format(score2))

if score1 >= 100 or score2 >= 100:
    if (score1 > score2):
        print(f"Player1 Wins!!!\nPlayer1^s score: {score1}\nPlayer2^s score: {score2}")
    elif (score1 == score2):
        print(f"Both of the players win!!!\nPlayer1^s score: {score1}\nPlayer2^s score: {score2}")
    else:
        print(f"Player2 Wins!!!\nPlayer2^s score: {score2}\nPlayer1^s score: {score1}")


