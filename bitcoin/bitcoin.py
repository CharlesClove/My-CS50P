import argparse
import sys
import requests

parser = argparse.ArgumentParser() #create praser from argprase library
parser.add_argument('amount',help="lets you pick font", type=float)  #add font argument as a

def main():
    try:
        args = parser.parse_args()
        if args.amount :
            raise ValueError
    except SystemExit as e:
        print("Command-line argument is not a number")
    except ValueError as e:
        print("Missing command-line argument")

main()
