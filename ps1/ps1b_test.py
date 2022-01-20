import unittest

from ps1b import months_for_down_payment


class Saving_with_a_raise(unittest.TestCase):
    def test1(self):
        months = months_for_down_payment(120000, .05, 500000, .03)
        self.assertEqual(months, 142)

    def test2(self):
        months = months_for_down_payment(80000, .1, 800000, .03)
        self.assertEqual(months, 159)

    def test3(self):
        months = months_for_down_payment(75000, .05, 1500000, .05)
        self.assertEqual(months, 261)
