import random
def main():
    random.seed()
    while(True):
        try:
            userInputLimit = int(input("Level: "))
            if userInputLimit <= 0:
                raise ValueError
        except ValueError:
            continue
        break
    randomNumber = random.randint(1,userInputLimit)
    while(True):
        try:
            userInputGuess = int(input("Guess: "))
        except ValueError:
            continue

        if userInputGuess == randomNumber:
            print("Just right!")
            break
        elif userInputGuess > randomNumber:
            print("Too large!")
        elif userInputGuess < randomNumber:
            print("Too small!")

main()
