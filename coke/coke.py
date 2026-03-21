#loop count downs from 50 till 0, if goes overboard prints 'owed' and stops program

def countdown():
    price = 50
    while price > 0:
        print(f"Amount Due: {price}")
        money = int(input("Insert Coin: "))
        if money is None or money is str:
            money = 0
        price -= money

    if price <= 0:
        print(f"Change Owed: {price*(-1)}")
def main():
    countdown()

main()
