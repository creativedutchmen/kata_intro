class Node(object):
    def get_value(self):
        raise NotImplementedError


class ValueNode(Node):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class OperatorNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PlusOperatorNode(OperatorNode):
    def get_value(self):
        return self.left.get_value() + self.right.get_value()


class MultiplyOperatorNode(OperatorNode):
    def get_value(self):
        return self.left.get_value() * self.right.get_value()
