
list_of_names=[]

while(True):
    try:
        inputted_name = input("Name: ")
        list_of_names.append(inputted_name)
    except EOFError:
        break

