def fuel(amount):
    p = round(amount)

    if p >= 99:
        return ("F")
    elif p <= 1:
        return ("E")
    else:
        return (f"{p}%")


def main():
    while(True):
        try:
            amount = input("Fraction: ")
            x, y = amount.split('/')
            try:
                amount = (float(x)/float(y))*100
            except ZeroDivisionError:
                print("zero division")
        except ValueError:
            print("Value")
            

    result = fuel(amount)

main()
