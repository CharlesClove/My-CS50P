u_input = input("Greeting: ").lower().strip().split()





def main():
    solution(u_input)

def value(greeting):
    if u_input[0].startswith('hello'):
        print('$0')
    elif str(u_input[0])[0] == "h":
        print('$20')
    else:
        print('$100')



if __name__ == "__main__":
    main()
