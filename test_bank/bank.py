def main():
    u_input = input("Greeting: ").lower().strip().split()
    print(value(u_input))

def value(greeting):
    if .startswith('hello'):
        return '$0'
    elif str(u_input[0])[0] == "h":
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()
