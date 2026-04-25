import random
#remember to use exceptions with ValueError!
# In a file called professor.py, implement a program that:

# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
import random

def main():
    random.seed()
    level = get_level()
    randomPairs = generate_integer(level)

    errorCounter = 3
    points = 10
    for f,s in randomPairs:
        for attempt in range(3):
            try:
                userAnwser = int(input(f"{f} + {s} = "))
                if userAnwser.is_integer() == False:
                    raise ValueError
                if userAnwser != (f + s):
                    errorCounter -= 1
                    raise ValueError
                else:
                    break
            except ValueError:
                if errorCounter == 0:
                    print(f"{f} + {s} = {f+s}")
                    points-1
                else:
                    print("EEE")
                    continue


def get_level():
    Choices = [1,2,3]
    while(True):
        try:
            userInputLevel = int(input("Level: "))
            if userInputLevel not in Choices:
                raise ValueError
        except ValueError:
            continue
        break
    return userInputLevel

def generate_integer(level):
    randomPairs=[]
    for i in range(9):
        if level == 1:
            randomPair = [random.randint(1,9),random.randint(1,9)]
        elif level == 2:
            randomPair = [random.randint(10,99), random.randint(10,99)]
        elif level ==3:
            randomPair = [random.randint(100,999), random.randint(100,999)]
        randomPairs.append(randomPair)
    return randomPairs

if __name__ == "__main__":
    main()
