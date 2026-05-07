def convert(fraction):
    ...


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return percentage

def main():
    while(True):
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            x = float(x)
            y = float(y)
            if x < 0 or x > y or x.is_integer() != True or y.is_integer() != True:
                raise ValueError
            fraction = (x/y)*100
            #print(f"{amount}  {type(amount)}")
        except (ValueError,ZeroDivisionError):
            continue
        break
    #print(f"3{amount}  {type(amount)}")
    print(percentage(round(fraction)))

if __name__ == "__main__":
    main()
