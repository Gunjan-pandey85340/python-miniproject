import random
player1s = 0
player2s = 0
for i in range(10):
    player1_value = random.randint(1,6)
    player2_value = random.randint(1,6)
    print("player1 rolled:",player1_value)
    print("player2 rolled:",player2_value)
    if player1_value > player2_value:
        print("player 1 wins")
        player1s = player1s+1
    elif player2_value>player1_value:
        print("player 2 wins")
        player2s = player2s+1
    else:
        print("it's a draw")
    input("press enter to continue")
print("##GAME OVER##")
print("player 1 score:",player1s)
print("player 2 score:",player2s)
