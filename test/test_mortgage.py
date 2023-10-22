import unittest

from src.mortgage import MortgageFlow


class TestMortgage(unittest.TestCase):
    def test_MortgageFlow_fixed_rate_constructor_should_create_the_flow_correctly(self):
        expected = MortgageFlow([-10, -1, -1, -1, -1, -1])

        result = MortgageFlow.fixed_rate(prepayment=10,
                                         number_of_period=5,
                                         monthly_payment=1)
        self.assertEqual(result, expected)
