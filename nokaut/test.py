from mock import MagicMock
import unittest
import lib


class SerwerTestCase(unittest.TestCase):

    def setUp(self):
        self.test = lib

    def tearDown(self):
        self.test = None

    def test1(self):
        parser = MagicMock(name="parser", return_value=("laptop",
                           "a8839b1180ea00fa1cf7c6b74ca01bb5"))
        api = lib.nokaut_api(parser())
        self.assertEqual(api, (
                         '1249,00',
                         'http://www.nokaut.pl/laptopy/toshiba-c850d-118.html'
                         ))

    def test2(self):
        parser = lib.parser(["-k", "laptop",
                             "a8839b1180ea00fa1cf7c6b74ca01bb5"])
        self.assertEqual(parser, ("laptop",
                         "a8839b1180ea00fa1cf7c6b74ca01bb5"))


if __name__ == "__main__":
    unittest.main()
