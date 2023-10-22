import unittest

from src.flow import *


class TestFlow(unittest.TestCase):
    def test_get_sum_should_return_the_sum_correctly(self):
        src = Flow([1, 2, 3, -4])
        expected = 2

        result = src.get_sum()
        self.assertEqual(result, expected)

    def test_get_sum_should_return_0_given_empty_flow(self):
        src = Flow([])
        expected = 0

        result = src.get_sum()

        self.assertEqual(result, expected)

    def test_merge_flows_should_add_the_flows_element_wise_given_one_input(self):
        src1 = Flow([1, 2, 3, -4, 10])
        src2 = Flow([-1, -2, -2, 4, 4])
        expected = Flow([0, 0, 1, 0, 14])

        result = src1.merge(flows=[src2])
        self.assertEqual(result, expected)

    def test_merge_flows_return_orig_flow_given_no_input(self):
        src = Flow([1, 2, 3, -4, 10])
        expected = Flow([1, 2, 3, -4, 10])

        result = src.merge(flows=[])
        self.assertEqual(result, expected)

    def test_merge_flows_should_add_the_flows_element_wise_given_any_number_of_input(self):
        src1 = Flow([1, 2, 3, 4, 5])
        src2 = Flow([-1, -2, -3, -4, -5])
        src3 = Flow([0, 1, 1, -1, 0])
        src4 = Flow([10, 20, 30, 40, 50])
        expected = Flow([10, 21, 31, 39, 50])

        result = src1.merge(flows=[src2, src3, src4])
        self.assertEqual(result, expected)

    def test_merge_flows_should_raise_error_if_flows_length_does_not_match(self):
        src1 = Flow([1, 2, 3, 4, 5])
        src2 = Flow([-1, -2, -3])
        with self.assertRaises(ValueError):
            src1.merge(flows=[src2])

    def test_a_flow_should_raise_init_error_if_multidim_array_is_give(self):
        src = np.random.rand(3, 2)
        with self.assertRaises(ValueError):
            Flow(src)

    def test_flow_add_raise_error_if_flows_length_does_not_match(self):
        src1 = Flow([1, 2, 3, 4, 5])
        src2 = Flow([-1, -2, -3])
        with self.assertRaises(ValueError):
            _ = src1 + src2

    def test_a_flow_can_be_initialized_with_python_list_too(self):
        src = [1, 2, 3]
        expected = Flow(src)

        result = Flow(src)
        self.assertEqual(result, expected)

    def test_a_flow_raises_error_if_payload_cannot_be_interpreted_as_int(self):
        with self.assertRaises(ValueError):
            _ = Flow(["1.0", "2.0", " 3.0"])
