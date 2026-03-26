def fuel(amount):
    #print(f"3 {amount}  {type(amount)}")
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
            x = float(x)
            y = float(y)
            if x < 0 and x > y:
                raise ValueError
            amount = (float(x)/float(y))*100
            #print(f"{amount}  {type(amount)}")
        except (ValueError,ZeroDivisionError):
            continue
        break
    #print(f"3{amount}  {type(amount)}")
    print(fuel(round(amount)))

main()
