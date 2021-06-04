import unittest
from optimal_change import optimal_change

class OptimalTest(unittest.TestCase):

    def test_type(self):
        self.assertEqual(type(optimal_change(62.13, 100)),str)

    def test_1(self):
        self.assertEqual(optimal_change(62.13, 100),"The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_2(self):
        self.assertEqual(optimal_change(31.51, 50),"The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

if __name__=='__main__':
    unittest.main()
