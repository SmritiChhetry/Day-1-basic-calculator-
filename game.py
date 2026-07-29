import random
print("lets play ROCK,PAPER,SCISSORS🎮🎮")
choices=["rock","paper","scissors"]
computer= random.choice(choices)
you=input("Choose rock,paper,scissor : ").lower()
print("COMPUTER=",computer,"Your choice=",you)
if you==computer:
    print("Its a tie.✨🎉")
elif (you=="rock" and computer=="scissors") or (you=="paper" and computer=="rock") or (you=="scissors" and computer=="paper"):
    print("YOU WIN !!!🎉🏆")
elif you in choices:
    print("COMPUTER WINS !!!🎉🏆")
else:
    print("INVALID CHOICE!!")