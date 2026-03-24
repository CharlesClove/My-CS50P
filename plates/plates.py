import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_min_max = [2,6]
    re_pattern = r'^[A-Z]{2,}([1-9][0-9]*)?$' # 'Allow' two or more letters. Numbers are optional '()?' , however first number cant be '0'
    if len(s)>plate_min_max[1] or plate_min_max[0]>len(s): #is the length good?
        return False
    else:
        return bool(re.fullmatch(re_pattern,s)) #does the s match the regex pattern? Not using findall because i want one exact match.



main()
