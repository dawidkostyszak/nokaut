import sys
import argparse


class Error:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", nargs=2, help="-k product key")

    try:
        args = parser.parse_args()
        if args.k is None:
            raise Error("lib.py usage: lib.py -k product key")
        else:
            return args.k
    except Error, error:
        print error
        sys.exit()
