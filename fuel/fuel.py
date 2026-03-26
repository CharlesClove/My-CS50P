def fuel(amount):
    percent = int(amount)
    if percent >= 99:
        print("F")

    elif percent <= 1:
        print("E")

    else:
        print(f"{percent}%")


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
