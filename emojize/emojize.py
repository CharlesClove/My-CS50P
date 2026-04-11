import emoji
import re
inputstr = input("Input: ")#I need to 'catch' string between ::
print(re.search(':*:', inputstr))
print(emoji.emojize(f'Output: {inputstr}'))

