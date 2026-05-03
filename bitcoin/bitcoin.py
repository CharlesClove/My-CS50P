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
        sys.exit(1)

    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=xxxxxx")
        response = r.json()
        bitcoinPrice = response["data"]["priceUsd"] #how to get into nested json data :D
    except requests.RequestException:
        print("Api error")
        sys.exit(3)
    amountToDollars = amount*float(bitcoinPrice)
    print(f"${amountToDollars:,.4f}")

main()
