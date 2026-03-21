def swap_to_snake(txt):
    for iteration in range(len(txt)):
        if isupper(txt[iteration]):
            print(txt[iteration])
            

def main():
    txt = input("camelCase:")
    swap_to_snake(str(txt))

main()
