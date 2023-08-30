from parser import *

def evalNode(node):
    if(type(node) == BinaryExpression):
        left = evalNode(node.left)
        operator = evalNode(node.operator)
        right = evalNode(node.right)
        if (operator == "+"):
            return left + right
        elif (operator == "-"):
            return left - right
        elif (operator == "*"):
            return left * right
        elif (operator == "/"):
            if(right != 0):
                return left / right
            else:
                print("error division by zero")
        else:
            print("error")
    if(type(node) == Literal):
        return node.value

def eval(ast):
    for node in ast:
        if(type(node) == BinaryExpression):
            print(evalNode(node))