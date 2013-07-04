import urllib
import urllib2
import sys
from lxml import etree


class Error:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def nokaut_api(key, product):

    url = 'http://api.nokaut.pl/'
    values = {
        'keyword': product,
        'method': 'nokaut.product.getByKeyword',
        'key': key,
        'format': 'xml'
    }
    data = urllib.urlencode(values)

    try:
        full_url = '?'.join([url, data])
        response = urllib2.urlopen(full_url, timeout=1)
        xml_file = response.read()
        response.close()
    except urllib2.URLError as err:
        return "No network connection"

    parse_xml = etree.fromstring(xml_file)
    if parse_xml.find('.//message') is not  None:
        return Error(" ".join(['Error:', parse_xml.find('.//message').text]))
    if parse_xml.find('.//item') is None:
        return Error("No products")

    url = parse_xml.find('.//url').text
    price = parse_xml.find('.//price_min').text
    return price, url

