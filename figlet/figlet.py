import pyfiglet
#f = pyfiglet.figlet_format("TEXT", font ="slant")
#print(f)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x') #must be used
praser.add_argument('--optional', help='its purely optional to use it', type=str)
args = parser.parse_args()
print(args.x)
