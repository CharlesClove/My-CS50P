def main():
    while(True):
        try:
            counter = 1
            list_item = input("Item: ")
            grocery_list = append(f"{counter}{list_item.upper()}")
            for item in grocery_list:
                print(item)
        except EOFError:
            break

main()
