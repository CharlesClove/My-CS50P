Fruits = {
    "apple":  130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100
}

def is_fruit(s):
   for name, kcal in Fruits.items():
      if s != name :
         pass
      else:
         print(f"Calories: {kcal}")

is_fruit(input("Item: "))
