Menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total=0.00
    while(True):
        try:
            order_input = input("Item: ")
            order = order_input.title()
            if order not in Menu.keys():
                raise ValueError
            order_value = Menu.get(order)
            total = total + order_value
            print(f"Total: ${total}")
        except ValueError:
            continue
        except EOFError:
            break







main()
