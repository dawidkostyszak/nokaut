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
    parser.add_argument("-k", nargs=2, help="-k key product")

    try:
        args = parser.parse_args()
        if args.k is None:
            raise Error("lib.py usage: lib.py -k key product")
        else:
            print nokaut_api(args.k[0], args.k[1])
    except Error, error:
        return error
