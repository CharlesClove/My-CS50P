def fuel(amount):
    p = round(amount)

    if p >= 99:
        print("F")
    elif p <= 1:
        print("E")
    else:
        print(f"{p}%")


def main():
    while(True):
        try:
            amount = input("Fraction: ")
            x, y = amount.split('/')
            try:
                amount = (float(x)/float(y))*100
            except ZeroDivisionError:
                pass
        except ValueError:
            pass
        fuel(amount)


main()
