def shorten(var_string):

    vovels = "aeiouAEIOU"
    var_cut_string = ""

    for iteration in range(len(var_string)):
        print(f"{vovels.find(var_string[iteration])} To jest wynik dla vovels.find ")
        if vovels.find(var_string[iteration]) != -1: #vovels.find() != -1 returns true if character is in string vovels
            var_cut_string += var_string[iteration].replace(var_string[iteration], "")
        else:
            var_cut_string += var_string[iteration]

    return var_cut_string


def main():
    to_cut = input("Input: ")
    cut_string = shorten(to_cut)
    print(f"Output: {cut_string}")

if __name__ == "__main__":
    main()
