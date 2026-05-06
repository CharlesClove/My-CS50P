def main():
    greeting = str(input("Greeting: ").strip().split())
    print(value(greeting))

def value(greeting):
    if greeting.lower().startswith('hello'):
        return '$0'
    elif greeting[0] == "h" or "H":
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()
