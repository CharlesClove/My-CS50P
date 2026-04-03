g_list = {}
def main():
    while(True):
        try:
            x = input()
            g_item = x.upper()
            if g_item in g_list.keys():
                g_list.update({g_item: g_list.get(g_item)+1})
            elif g_item not in g_list.keys():
                g_list.setdefault(g_item,1)
        except EOFError:
            break
    print(dict(sorted(g_list.items())))


main()
