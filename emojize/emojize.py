import emoji
import re

#inputstr = ":candy: or :ice_cream:?"
inputstr = input("Input: ").strip() #I need to 'catch' string between ::
match = re.split(r"(:\w+:)", inputstr) #I like re
new_list = [] # new list to append with emojized words. probably could be done better.
for word in match:
    new_list.append(emoji.emojize(word, language = "alias"))
print(f"Output: {"".join(new_list)}") #joins new_list elements into single string
