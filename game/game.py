import random
def main():
    random.seed()
    while(True):
        try:
            userInputLimit = int(input("Level: "))
        except ValueError:
            continue
        break
    randomNumber = random.randint(1,userInputLimit)
    while(True):
        try:
            userInputGuess = int(input("Guess: "))
        except ValueError:
            continue
        break
        if userInputGuess == randomNumber:
            print("Just right!")
        elif userInputGuess > randomNumber:
            print("Too large!")
        elif userInputGuess < randomNumber:
            print("Too large!")

main()
