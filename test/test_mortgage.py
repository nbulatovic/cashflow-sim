import unittest

from src.mortgage import MortgageFlow


class TestMortgage(unittest.TestCase):
    def test_MortgageFlow_fixed_rate_constructor_should_create_the_flow_correctly(self):
        expected = MortgageFlow([1, 1, 1, 1, 1])

        result = MortgageFlow.fixed_rate(term=5, price=1)
        self.assertEqual(result, expected)
