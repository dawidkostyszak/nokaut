import sys
import argparse
from lib import nokaut_api


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", nargs=2, help="-k key product")

    args = parser.parse_args()
    if args.k is None:
        print "lib.py usage: lib.py -k key product"
    else:
        print nokaut_api(args.k[1], args.k[0])
