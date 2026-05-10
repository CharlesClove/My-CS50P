import argparse
import sys
__parse = argparse.ArgumentParser()
__parse.add_argument('test',nargs=1 )


def main():
    print(sys.argv)
    args = __parse.parse_args()
    ...
    print(args.test)

if __name__ == "__main__":
    main()
