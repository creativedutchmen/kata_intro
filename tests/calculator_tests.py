from calculator.nodes import Node, ValueNode, OperatorNode, PlusOperatorNode
from nose.tools import assert_equals, raises


class testCalculator():
    @raises(NotImplementedError)
    def test_not_implemented(self):
        node = Node()
        node.get_value()

    def test_value_node(self):
        node = ValueNode(4)
        assert_equals(node.get_value(), 4)

    def test_plus(self):
        left = ValueNode(4)
        right = ValueNode(-1)
        operator = PlusOperatorNode(left, right)
        assert_equals(operator.get_value(), 3)

    def nested_test(self):
        left = ValueNode(7)
        right = PlusOperatorNode(
            ValueNode(4), ValueNode(-1)
        )
        operator = PlusOperatorNode(left, right)
        assert_equals(operator.get_value(), 10)
