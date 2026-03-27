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

def calculate_order(order):
    

def main():
    while(True):
        try:
            order = input("Item: ")
            if order not in Menu.keys():
                print(f"{order}")
                raise ValueError
        except ValueError:
            print(f"Wrong Value")
            continue
        calculate_order(order)






main()
