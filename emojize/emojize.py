import emoji
import re

inputstr = input("Input: ")#I need to 'catch' string between ::
match = re.match(r":._*:", inputstr)
if match:
    print(match.group())
else:
    print("no match")
#print(emoji.emojize(f'Output: {inputstr}'))

