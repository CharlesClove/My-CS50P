import sys
list_of_names=[]
adieu_string = "Adieu, adieu, to "
in_list_name_counter = 0

while(True):
    try:
        inputted_name = input("Name: ")
        list_of_names.append(inputted_name)
    except EOFError:
        print()
        break
#list stores names , len returns number of names inside
if not list_of_names:
    print("List cannot be empty!")
    sys.exit()
elif len(list_of_names) == 1:
    print(f"{adieu_string}{list_of_names[0]}")
elif len(list_of_names) == 2:
    print(f"{adieu_string}{list_of_names[0]} and {list_of_names[len(list_of_names)-1]}")
else:
    print(f"{adieu_string}{list_of_names[0]}{", ".join(list_of_names[1:-1])}, and {list_of_names[len(list_of_names)-1]}")
