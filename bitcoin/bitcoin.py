import argparse
import sys
import requests

parser = argparse.ArgumentParser() #create praser from argprase library
parser.add_argument('amount',help="write amount of bitcoin to see value in $")  #add font argument as a

def main():
    try:
        args = parser.parse_args()
        if not isinstance(args.amount, float):
            raise ValueError
    except SystemExit as e:
        print("Missing command-line argument")
    except ValueError as e:
        print("Command-line argument is not a number")


main()
