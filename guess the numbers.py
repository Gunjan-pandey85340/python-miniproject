import random
n = input("enter your name  ")
b = int(input("starting value"))
c = int(input("ending value"))
att = 6
out = random.randint(b,c)
while att:
    n = int(input("enter the number"))
    if n < out:
        print("number is too small")
    elif n > out:
        print("number is too large")
    elif n==out:
        print("you guess correctly")
        print("yeah!you win the game")
    else:
        print("you lose the game")
    print("only"+str(att)+"attempt left")
    att -= 1
    
