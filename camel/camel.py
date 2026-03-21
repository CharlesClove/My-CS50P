def swap_to_snake(txt):
    snake_text = ""
    for iteration in range(len(txt)):
        print(f"iteration numer: {iteration}")
        if txt[iteration].isupper():
            snake_text += "".join(txt[iteration].replace(f"{txt[iteration]}", f"_{txt[iteration].lower()}"))
        else:
            snake_text += "".join(txt[iteration])
        print(f"snake - {snake_text}")
    print(f"snake_case: {snake_text}")


def main():
    txt = input("camelCase: ")
    swap_to_snake(str(txt))

main()

