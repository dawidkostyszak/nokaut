import urllib
import urllib2
from lxml import etree


class NokautError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def nokaut_api(product, key):

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
        raise NokautError("No network connection")

    parse_xml = etree.fromstring(xml_file)
    message = parse_xml.find('.//message')
    if message is not None:
        raise NokautError(message.text)

    if parse_xml.find('.//item') is None:
        raise NokautError("No products")

    url = parse_xml.find('.//url').text
    change_coma = (parse_xml.find('.//price_min').text).replace(',', '.')
    price_float = float(change_coma)

    return price_float, url
