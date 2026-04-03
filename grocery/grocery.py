def main():
    while(True):
        try:
            g_list = {}
            g_item = input("Input: ")
            if g_item in g_list.keys():
                print("apple+1")
            elif g_item not in g_list.keys():
                g_list.setdefault(g_item,1)
        except EOFError:
            break
        print(g_list)

main()
