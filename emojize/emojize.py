import emoji
inputstr = input("Input: ")#I need to 'catch' string between ::
str1, str2 = inputstr.split(':')
print(emoji.emojize(f'Output: {inputstr}'))

