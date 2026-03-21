#loop count downs from 50 till 0, if goes overboard prints 'owed' and stops program

def countdown()
    price = 50
    while price > 0:
        print(f"Amount due: {price}")
        money = input("Insert coin: ")
        price -= money

    if price <= 0:
        print(f"Change owed: ")
def main()
    countdown()
main()
