def swap_to_snake(txt):
    for iteration in range(len(txt)):
        if txt[iteration].isupper():
            txt[iteration] = txt[iteration].replace(f"{txt[iteration]}", f"_{txt[iteration].lower()}")
            print(txt)


def main():
    txt = input("camelCase:")
    swap_to_snake(str(txt))

main()

