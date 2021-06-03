import unittest
from packages.print_options_list import provide_options

class TestProvideOptions(unittest.TestCase):
    def test_provide_options(self):
        result = provide_options()
        self.assertEqual(result, '')