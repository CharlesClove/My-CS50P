u_input = input("Greeting: ").lower().strip().split()

def solution(u_input):
    if u_input[0].startswith('hello'):
        print('$0')
    elif str(u_input[0])[0] == "h":
        print('$20')
    else:
        print('$100')

solution(u_input)
