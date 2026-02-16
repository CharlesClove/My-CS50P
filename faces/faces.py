def swap(string):
    swapped_string = string.replace(":)","😊")
    swapped_string = string.replace(":(","☹️")
    print(swapped_string)
    return swapped_string

print(swap(input()))
