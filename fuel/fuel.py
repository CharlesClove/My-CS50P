def fuel(percent):
    try
    ...
def main():
    amount = input("Fraction: ")
    x, y = amount.split('/')
    amount = (float(x)/float(y))*100
    fuel(amount)
main()
