import urllib
import urllib2
import sys
from lxml import etree


class Error:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


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
        if parse_xml.find('.//message') is None:
            url = parse_xml.find('.//url').text
            price = parse_xml.find('.//price_min').text
            print price, url
        else:
            raise Error(" ".join(['Error:',
                                 parse_xml.find('.//message').text]))
    except Error, error:
        print error
        sys.exit()

#python lib.py -k laptop a8839b1180ea00fa1cf7c6b74ca01bb5
nokaut_api(parser())
