import unittest

from src.flow import Flow
from src.mortgage import MortgageFlow


class TestMortgage(unittest.TestCase):

    def test_MortgageFlow_should_be_initializable_from_other_flow(self):
        src = Flow([-10, -1, -1, -1, -1, -1])
        expected = MortgageFlow([-10, -1, -1, -1, -1, -1])

        result = MortgageFlow.from_flow(src)
        self.assertEqual(result, expected)

    def test_MortgageFlow_fixed_rate_constructor_should_create_the_flow_correctly(self):
        expected = MortgageFlow([-10, -1, -1, -1, -1, -1])

        result = MortgageFlow.fixed_rate(prepayment=10,
                                         number_of_period=5,
                                         monthly_payment=1)
        self.assertEqual(expected, result)
