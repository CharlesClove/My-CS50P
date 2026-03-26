def fuel(amount):
    percent = int(round(amount))
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
        amount = (float(x)/float(y))*100
    except (ValueError, ZeroDivisionError):
        print("")
    fuel(amount)

main()
