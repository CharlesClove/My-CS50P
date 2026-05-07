def convert(fraction):
    x, y = fraction.split('/')
    x = float(x)
    y = float(y)
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x < 0 or x > y or x.is_integer() != True or y.is_integer() != True:
        raise ValueError
    return (x/y)*100


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return f"{percentage}%"

def main():
    while(True):
        try:
            fraction = input("Fraction: ")
            fraction = convert(fraction)
        except (ValueError,ZeroDivisionError):
            continue
        break
    print(gauge(round(fraction)))

if __name__ == "__main__":
    main()
