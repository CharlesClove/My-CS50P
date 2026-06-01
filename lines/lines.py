import argparse
import sys
import re
__parse = argparse.ArgumentParser()
__parse.add_argument('file')

class TooFewArgs(Exception):
    pass
class TooManyArgs(Exception):
    pass
class WrongFile(Exception):
    pass


def checkTheArguments(numberOfArgs:int) -> bool:
    re_pattern = r'.*\.py$'
    try:
        if numberOfArgs <= 0:
            raise TooFewArgs
        if numberOfArgs >= 2:
            raise TooManyArgs
        if not re.search(re_pattern, sys.argv[1]):
            raise WrongFile
        return True
    except TooFewArgs:
        print("Too few command-line arguments ")
    except TooManyArgs:
        print("Too many command-line arguments ")
    except WrongFile:
        print("Not a Python file")
    return False

def checkTheFile(args) -> int:
    Nlines = 0
    in_docstring = False
    try:
        with open(args.file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        return 0

    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            Nlines += 1

    return Nlines

def main():
    numberOfArgs: int = len(sys.argv)-1
    if checkTheArguments(numberOfArgs):
        args = __parse.parse_args()
        lines = checkTheFile(args)
        print(lines)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
