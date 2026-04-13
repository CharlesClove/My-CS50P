import emoji
import re

inputstr = input("Input: ")#I need to 'catch' string between ::
match = re.split(r":\w*:", inputstr)
print(match)
\

