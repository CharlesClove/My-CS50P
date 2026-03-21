def swap_to_snake(txt):
    for iteration in range(len(txt)):
        snake_text=""
        if txt[iteration].isupper():
            snake_text.join(txt[iteration].replace(f"{txt[iteration]}", f"_{txt[iteration].lower()}"))
        snake_text.join(txt[iteration])
        print(f"snake_case: {snake_text}")


def main():
    txt = input("camelCase: ")
    swap_to_snake(str(txt))

main()

