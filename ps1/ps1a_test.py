import unittest

from ps1a import months_for_down_payment


class House_Hunting(unittest.TestCase):
    def test1(self):
        months = months_for_down_payment(120000, .10, 1000000)
        self.assertEqual(months, 183)

    def test2(self):
        months = months_for_down_payment(80000, .15, 500000)
        self.assertEqual(months, 105)
