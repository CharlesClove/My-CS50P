import emoji
import re

inputstr = input("Input: ")#I need to 'catch' string between ::
match = re.match(":*:", inputstr)
if match:
    print(match.group(1))
#print(emoji.emojize(f'Output: {inputstr}'))

