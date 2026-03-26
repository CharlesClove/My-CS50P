def fuel(amount):
    print(f"2 {amount}  {type(amount)}")
    if amount >= 99:
        return ("F")
    elif amount <= 1:
        return ("E")
    else:
        return (f"{amount}%")


def main():
    while(True):
        try:
            amount = input("Fraction: ")
            x, y = amount.split('/')
            try:
                amount = (float(x)/float(y))*100
                print(f"{amount}  {type(amount)}")
            except ZeroDivisionError:
                pass
        except ValueError:
            pass
        break

    print(fuel(amount))

main()
