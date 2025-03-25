import unittest
from task2 import sum_monetary_amounts  # Імпортуємо функцію з вашого модуля

class TestSumMonetaryAmounts(unittest.TestCase):

    def test_basic_case(self):
        text = "first amount is $123.45, second amount is $400"
        self.assertAlmostEqual(sum_monetary_amounts(text), 523.45)

    def test_multiple_amounts(self):
        text = "Prices: $10.50, $20, $30.75 and $40.25"
        self.assertAlmostEqual(sum_monetary_amounts(text), 101.50)

    def test_no_amounts(self):
        text = "No monetary amounts here"
        self.assertEqual(sum_monetary_amounts(text), 0.0)

    def test_integers_only(self):
        text = "$100 $200 $300"
        self.assertEqual(sum_monetary_amounts(text), 600.0)

    def test_decimals_only(self):
        text = "$1.11 $2.22 $3.33"
        self.assertAlmostEqual(sum_monetary_amounts(text), 6.66)

    def test_mixed_formats(self):
        text = "Amounts: $5, $10.50, $15.75, $20"
        self.assertAlmostEqual(sum_monetary_amounts(text), 51.25)

if __name__ == '__main__':
    unittest.main()