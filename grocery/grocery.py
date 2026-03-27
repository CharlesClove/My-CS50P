def main():
    while(True):
        try:
            counter = 1
            list_item = input("Item: ")
            order = append(f"{}{list_item.upper()}")
        except ValueError:
            continue
        except EOFError:
            break

main()
