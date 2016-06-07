class Node(object):
    def __init__(self, left, right=None, operator=None):
        self.left = left
        self.right = right
        self.operator = operator

    def get_value(self):
        if self.operator == '+':
            return self.left.get_value() + self.right.get_value()
        elif self.operator == '-':
            return self.left.get_value() - self.right.get_value()
        elif self.operator == '*':
            return self.left.get_value() * self.right.get_value()
        elif self.operator == '/':
            return self.left.get_value() / self.right.get_value()
        elif self.operator is None:
            return self.left
        else:
            raise TypeError
