
def math_interpreter(question):
    list_of_characters = question.split(" ")
    if len(list_of_characters) == 3:
        match list_of_characters[1]:
            case '+': return float(list_of_characters[0])+float(list_of_characters[2])
            case '*': return float(list_of_characters[0])*float(list_of_characters[2])
            case '/': return float(list_of_characters[0])/float(list_of_characters[2])
            case '-': return float(list_of_characters[0])-float(list_of_characters[2])
            case _: return "invalid expression"
    else:
        return "invalid expression"

question = input("Expression: ")
solution = math_interpreter(question)
#solution = float(math_interpreter(question))
print(f"{solution}")
