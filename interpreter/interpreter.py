
def math_interpreter(question):
    list_of_characters = question.split(" ")
    list_of_characters.sort()
    return list_of_characters

question = input("Expression: ")
solution = math_interpreter(question)
#solution = float(math_interpreter(question))
print(f"{solution}")
