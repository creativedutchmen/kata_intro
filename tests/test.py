from intro.intro import Node

from nose.tools import assert_equals, raises


class testCalculator():
    def test_sum(self):
        left = Node(2)
        right = Node(4)
        calculation = Node(left, right, '+')
        assert_equals(calculation.get_value(), 6)

    def test_min(self):
        left = Node(2)
        right = Node(4)
        calculation = Node(left, right, '-')
        assert_equals(calculation.get_value(), -2)

    def test_product(self):
        left = Node(2)
        right = Node(4)
        calculation = Node(left, right, '*')
        assert_equals(calculation.get_value(), 8)
