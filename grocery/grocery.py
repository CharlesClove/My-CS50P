def main():
    while(True):
        try:
            order_input = input("Item: ")
            order = order_input.upper()
            if order not in Menu.keys():
                raise ValueError
            order_value = Menu.get(order)
            total = total + order_value
            print(f"Total: ${total:.2f}")
        except ValueError:
            continue
        except EOFError:
            break

main()
