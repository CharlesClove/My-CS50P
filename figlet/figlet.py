import pyfiglet
#f = pyfiglet.figlet_format("TEXT", font ="slant")
#print(f)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x',type=int) #must be used, the int is accessed in args.x
praser.add_argument('--optional', help='its purely optional to use it', type=str, default=0, action="count")
args = parser.parse_args()
print(args.x)
