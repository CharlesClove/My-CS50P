import argparse
import sys
import requests

parser = argparse.ArgumentParser() #create praser from argprase library
parser.add_argument('amount',help="write amount of bitcoin to see value in $")  #add font argument as a

def main():
    try:
        args = parser.parse_args()
    except SystemExit:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        amount = float(args.amount)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(2)

    try:
        r.requests.get()
    except requests.RequestException:
    ...


main()
