def main():
    while(True):
        try:
            
            counter = 1
            grocery_list = []
            list_item = input("Item: ")
            if old_list_item == list_item:
                counter += 1
            grocery_list.append(f"{counter} {list_item.upper()}")
            for item in grocery_list:
                print(item)
            old_list_item = list_item
        except EOFError:
            break

main()
