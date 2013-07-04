import sys
import argparse
from lib import nokaut_api


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
            nokaut_api(args.k)
    except Error, error:
        print error
        sys.exit()
