import sys
list_of_names=[]
adieu_string = "Adieu, adieu, to "
while(True):
    try:
        inputted_name = input("Name: ")
        list_of_names.append(inputted_name)
    except EOFError:
        break
#list stores names , len returns number of names inside
if not list_of_names:
    print("List cannot be empty!")
    sys.exit()

