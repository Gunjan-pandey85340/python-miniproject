import random
ls = ['rock','paper','scissor']
out = random.choice(ls)#CHOICE OF COMPUTER
player =  input("player choice ")
if out == player:
    print("GAME IS TIE")
elif(out==rock and player == paper):
    print("player win the game")
elif(out == paper and player == scissor):
    print("player with the game")
else:
    print("you loose the game")
