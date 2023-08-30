class BinaryExpression:
    def __init__(self, left, operator, right ):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryExpression(left:{self.left}, operator:{self.operator}, right:{self.right})"

class Literal:
    def __init__(self, value ):
        self.value = value

    def __repr__(self):
        return f"Literal(value:{self.value})"

