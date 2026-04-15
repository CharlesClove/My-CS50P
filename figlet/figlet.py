#import pyfiglet
#f = pyfiglet.figlet_format("TEXT", font ="slant")
#print(f)
import random
from pyfiglet import Figlet
random.seed()
figlet = Figlet()
figfonts = figlet.getFonts()

import argparse

parser = argparse.ArgumentParser()

# parser.add_argument('x',type=int) #must be used, the int is accessed in args.x
# praser.add_argument('--optional', help='its purely optional to use it', type=str, default=0, action="count")
parser.add_argument('text', type=str)
parser.add_argument('-f','--font', help="lets you pick font", action="store_true")
parser.add_argument('font', help="write name of font", type=str)

args = parser.parse_args()
if args.font == 1:
    figlet.setFont(font=args.font)
    print(
        figlet.renderText(args.text))
else:
    figlet.setFont(font=random.choice(figfonts))
    print(
        figlet.renderText(args.text))

