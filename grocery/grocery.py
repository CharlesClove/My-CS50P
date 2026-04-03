g_list = {}
def main():
    while(True):
        try:
            x = input("Input: ")
            print(x)
            g_item = x.upper()
            if g_item in g_list.keys():
                g_list.update({g_item: g_list.get(g_item)+1})
            elif g_item not in g_list.keys():
                g_list.setdefault(g_item,1)
        except EOFError:
            break
        print(g_list.get())

main()
