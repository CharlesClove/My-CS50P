def fuel(percent):

    ...
def main():
    try:
        amount = input("Fraction: ")
        x, y = amount.split('/')
        amount = (float(x)/float(y))*100
    except(ValueError):
        
    fuel(amount)

main()
