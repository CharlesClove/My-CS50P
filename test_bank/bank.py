def main():
    greeting = str(input("Greeting: ").lower().strip().split())
    print(value(greeting))

def value(greeting):
    greeting.lower()
    if greeting.startswith('hello'):
        return '$0'
    elif greeting[0] == "h":
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()
