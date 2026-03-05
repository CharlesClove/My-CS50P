
def math_interpreter(question):
    list_of_characters = question.split(" ")
    if len(list_of_characters) == 3:
        list_of_characters.sort()
        
        return list_of_characters
    else:
        return "invalid expression"

question = input("Expression: ")
solution = math_interpreter(question)
#solution = float(math_interpreter(question))
print(f"{solution}")
