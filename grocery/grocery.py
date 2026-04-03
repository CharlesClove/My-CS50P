def main():
    while(True):
        try:
            g_list = {}
            g_item = input("Input: ")
            if key in g_list:
                g_list.get(key)+1
            elif key not in g_list:
                g_list.setdefault(g_item,1)
        except EOFError:
            break
        print(g_list)

main()
