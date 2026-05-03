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
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=25406b28524673f63ad7bc9c901b056265b01de076fd9ef72dc6eebb30f5b905")
        response = r.json()
        bitcoinPrice = response["data"]["priceUsd"]
    except requests.RequestException:
        print("Api error")
        sys.exit(3)
    amountToDollars = amount*float(bitcoinPrice)
    print(f"${amountToDollars}")

main()
