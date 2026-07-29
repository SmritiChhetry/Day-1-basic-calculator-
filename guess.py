import random
secret_number = random.randint(1,200)
while True:
    guess=int(input(" 🤔Guess a number between 1 to 200 : "))
    if guess>secret_number:
        print("Smaller ⬇")
    elif guess<secret_number:
        print("larger ⬆")
    else:
        print("CONGRATULATIONS!!! 🤩🎉YOU GUESSED CORECTLY")
        print("🏆🏆 You win")
        break
