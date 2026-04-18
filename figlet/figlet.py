
#import pyfiglet
#f = pyfiglet.figlet_format("TEXT", font ="slant")
#print(f)
import sys
import random
from pyfiglet import Figlet
import argparse

random.seed() # seed to randomise
figlet = Figlet() #create figlet object
figfonts = figlet.getFonts() #get fonts from Figlet library
parser = argparse.ArgumentParser() #create praser from argprase library

# parser.add_argument('x',type=int) #must be used, the int is accessed in args.x
# praser.add_argument('--optional', help='its purely optional to use it', type=str, default=0, action="count")

parser.add_argument('-f','--font',help="lets you pick font", type=str)  #add font argument as a
                                                                        #str type which waits for str after calling this arg
args = parser.parse_args() #prase arguments into object with type

if args.font != None: #if font was created
    if args.font not in figfonts: #check if font in CLI exists withing library of figlet
        sys.exit("Invalid usage fonts") #call error if it's not in there
    figlet.setFont(font=args.font) #set font to the CLI argument
    textToFiglet = input("Input:") #input text to render
    print(
        figlet.renderText(textToFiglet))

else: #if args.font does not exists use random seed and randomise font from library
    figlet.setFont(font=random.choice(figfonts))
    textToFiglet = input("Input:")

    print(
        figlet.renderText(textToFiglet))

