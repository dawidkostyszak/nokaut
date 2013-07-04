import urllib
import urllib2
import sys
import argparse
from lxml import etree


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
        if not args.k:
            raise Error("lib.py usage: lib.py -k product key")
        else:
            return args.k
    except Error, error:
        print error
        sys.exit()


def nokaut_api(argv):
    product, key = argv

    url = 'http://api.nokaut.pl/'
    values = {'keyword': product,
              'method': 'nokaut.product.getByKeyword',
              'key': key,
              'format': 'xml'}
    data = urllib.urlencode(values)

    try:
        response = urllib2.urlopen(''.join([url, '?', data]), timeout=1)
        xml_file = response.read()
        response.close()
    except urllib2.URLError as err:
        print "No network connection"
        sys.exit()

    try:
        parse_xml = etree.fromstring(xml_file)
        if not parse_xml.find('.//message'):
            url = parse_xml.find('.//url').text
            price = parse_xml.find('.//price_min').text
            print price, url
        else:
            raise Error("Error: wrong xml key")
    except Error, error:
        print error
        sys.exit()

#python lib.py -k laptop a8839b1180ea00fa1cf7c6b74ca01bb5
nokaut_api(parser())
