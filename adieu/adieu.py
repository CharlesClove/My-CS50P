import sys
list_of_names=[]
adieu_string = "Adieu, adieu, to "
in_list_name_counter = 0
arr = ['a','b']
print(' '.join(str(j) for j in arr))
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



# for i in range(len(list_of_names)-1):
#     if i == 0:
#         adieu_string += list_of_names[i]
#     else:
#         ", ".join()
# print(adieu_string)
