import pyfiglet
#f = pyfiglet.figlet_format("TEXT", font ="slant")
#print(f)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x')
args = parser.parse_args()
print(args.x)
