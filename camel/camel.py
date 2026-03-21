def swap_to_snake(txt):
    for iteration in range(len(txt)):
        if txt[iteration].isupper():
            txt[iteration].replace(f"{txt[iteration]}", f"_{txt[iteration].tolower()}")
            print(txt)

def main():
    txt = input("camelCase:")
    swap_to_snake(str(txt))

main()

