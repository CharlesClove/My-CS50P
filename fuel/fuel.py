def fuel(percent):
    print(f"{int(round(percent))}%")
    ...
def main():
    try:
        amount = input("Fraction: ")
        x, y = amount.split('/')
        amount = (float(x)/float(y))*100
    except (ValueError, ZeroDivisionError):
        print("")
    fuel(amount)

main()
