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

for i in range(len(list_of_names)-1):
    if i == 1:
        adieu_string += list_of_names[i]
    else:
        adieu_string += ", ".join(list_of_string[i])

print(adieu_string)
