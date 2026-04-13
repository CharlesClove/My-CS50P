import emoji
import re

inputstr = input("Input: ")#I need to 'catch' string between ::
match = re.match(r":*:", inputstr)
if match:
    print(match.group(1))
else:
    print("no match")
#print(emoji.emojize(f'Output: {inputstr}'))

