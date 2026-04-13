import emoji
import re

def matching_str(match):
    if match:
        print(match.group())
    else:
        print("no match")

inputstr = input("Input: ")#I need to 'catch' string between ::
match = re.match(r":\w*:", inputstr)
split_str = inputstr.split(match.group(), 1)

#matching_str(match)
#print(emoji.emojize(f'Output: {inputstr}'))

