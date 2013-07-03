import urllib
import sys
import getopt
from lxml import etree


def parser(argv):

    product = ''
    key = ''

    try:
        opts, args = getopt.getopt(argv, "k", ["keys="])
    except getopt.GetoptError:
        print 'test.py -k <product> <key>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -k <product> <key>'
            sys.exit()
        elif opt in ("-k", "--keys"):
            product = args[0]
            key = args[1]

    if opts:
        return product, key
    else:
        print 'test.py -k <product> <key>'
        sys.exit(2)


def nokaut_api(argv):

    product, key = argv

    sock = urllib.urlopen("http://api.nokaut.pl/?format=xml&key=" +
                          key +
                          "&method=nokaut.product.getByKeyword&keyword=" +
                          product +
                          "&filters[price][from]=1200&filters[price][to]=2200")
    htmlSource = sock.read()
    sock.close()

    root = etree.XML(htmlSource)
    price = "2300,00"

    path = root.xpath("node()")
    path2 = path[1].xpath("node()")

    for i in range(1, len(path2), 2):
        path3 = path2[i].xpath("node()")
        if path3[9].text < price:
            price = path3[9].text
            url = path3[15].text

    return price, url


if __name__ == "__main__":
    parse = parser(sys.argv[1:])
    print nokaut_api(parse)
