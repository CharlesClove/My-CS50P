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
    total=0.
    while(True):
        print(total)
        try:
            order = input("Item: ")
            if order.capitalize() not in Menu.keys():
                print(f"Value Error dla {order}")
                raise ValueError
            order_value = Menu.get(order)
            total = total + order_value
            print(f"Total: {total}")
        except ValueError:
            continue
        except EOFError:
            break







main()
