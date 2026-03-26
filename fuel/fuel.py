def fuel(amount):
    percent = int(amount)
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")

def main():
    try:
        amount = input("Fraction: ")
        x, y = amount.split('/')

        if float(x) >= 0 and float(y) > 0:
            amount = round((float(x)/float(y))*100)

    except (ValueError, ZeroDivisionError):
        pass
    fuel(amount)

main()
