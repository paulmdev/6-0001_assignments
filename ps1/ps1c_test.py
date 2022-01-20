import unittest

from ps1c import get_saving_rate_for_down_payment


class Finding_the_right_amount_to_save_away(unittest.TestCase):
    """
    I didn't test for the exact steps in bisection search because, as the problem set says,
    different implementation of the algorithm gives a different step value.

    Also, the savings_rate are almost equal taking only two decimal places.
    """

    def test1(self):
        savings_rate, step_bi_search = get_saving_rate_for_down_payment(150000)
        self.assertAlmostEqual(savings_rate, 0.4411, 2)

    def test2(self):
        savings_rate, step_bi_search = get_saving_rate_for_down_payment(300000)
        self.assertAlmostEqual(savings_rate, 0.2206, 2)

    def test3(self):
        with self.assertRaises(Exception):
            get_saving_rate_for_down_payment(10000)
