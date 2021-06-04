import unittest
from optimal_change import optimal_change

class OptimalTest(unittest.TestCase):

    def test_type(self):    #output should always be a string
        self.assertEqual(type(optimal_change(62.13, 100)),str)

    def test_not_enough(self):  #test case not enough payment
        self.assertEqual(optimal_change(62.13, 50),'The payment was not enough. The amount still owed is $12.13.')
    
    def test_alpha_input(self):  #test case non numeric input
        self.assertEqual(optimal_change('a', 'b'),'Invalid inputs: inputs must be numeric.')
    
    def test_perfect_change(self):  #test case give exact change
        self.assertEqual(optimal_change(50, 50),'You payed the perfect amount. No changed will be dispensed. You make my job easy. I love you!')

    def test_1(self):   #given test case 1
        self.assertEqual(optimal_change(62.13, 100),"The optimal change for an item that costs $62.13 with an amount paid of $100.00 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_2(self):   #given test case 2
        self.assertEqual(optimal_change(31.51, 50),"The optimal change for an item that costs $31.51 with an amount paid of $50.00 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_3(self):   #integer inputs, high change
        self.assertEqual(optimal_change(25, 10000),"The optimal change for an item that costs $25.00 with an amount paid of $10000.00 is 99 $100 bills, 1 $50 bill, 1 $20 bill, and 1 $5 bill.")

    def test_4(self):   #low case single coin output
        self.assertEqual(optimal_change(0.01, 0.02),"The optimal change for an item that costs $0.01 with an amount paid of $0.02 is 1 penny.")

    def test_5(self):   #normal case single bill output
        self.assertEqual(optimal_change(45.00, 50.00),"The optimal change for an item that costs $45.00 with an amount paid of $50.00 is 1 $5 bill.")

if __name__=='__main__':
    unittest.main()
