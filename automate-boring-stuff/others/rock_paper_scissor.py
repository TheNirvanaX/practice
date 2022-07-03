# This is rock-paper-scissor game
from re import S
import sys, random
print("Welcome! to Rock-Paper-Scissor")
win,loss,draw=0,0,0
while True:
    print("Score: Wins:"+str(win)+" loss:"+str(loss)+" draw:"+str(draw))
    print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
    user_input=input()
    if user_input=='q':
        sys.exit()

    com=random.choice(["p","s","r"])
    
    if user_input=="p":
        print("Paper versus .....")
    elif user_input=="r":
        print("Rock versus .....")
    elif user_input=="s":
        print("Scissor versus .....")

    if com=="p":
        print("Paper")
    elif com=="r":
        print("Rock")
    elif com=="s":
        print("Scissor")

    if com==user_input:
        print("It is a Draw!")
        draw+=1
    elif com=='r' and user_input=='p':
        print("You win!")
        win+=1
    elif com=='r' and user_input=='s':
        print("You lose!")
        loss+=1
    elif com=='p' and user_input=='r':
        print("You lose!")
        loss+=1
    elif com=='p' and user_input=='s':
        print("You win!")
        win+=1
    elif com=='s' and user_input=='r':
        print("You win!")
        win+=1
    elif com=='s' and user_input=='p':
        print("You loss!")
        loss+=1