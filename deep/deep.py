

def the_deep_anwser(user_input):
    if user_input == '42' or user_input.lower() == 'forty-two' or user_input.lower() == 'forty two':
        print('Yes')
    else:
        print('No')

user_input = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
the_deep_anwser(user_input)

