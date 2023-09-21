from lexer import *
from asttypes import *

class Parser:
    def __init__(self, listOfTok):
        self.listOfTok = listOfTok

    index = 0
    
    def nextTok(self):
        self.index += 1

    def getNextTok(self):
        if(self.index < len(self.listOfTok) - 1):
            return self.listOfTok[self.index + 1].type

    def getTok(self):
        return self.listOfTok[self.index]
    
    def accept(self, tok):
        if (self.getNextTok() == tok):
            self.nextTok()
            return True
        else:
            return False

    def parseParen(self):
        if (self.getTok().type == Tok.LEFT_PAREN):
            self.nextTok()
            expr = self.parseExpression()
            if(self.accept(Tok.RIGHT_PAREN)):
                return expr
        else:
            literal = self.parseLiteral()
            return literal
        
    def parseLiteral(self):
        return Literal(self.getTok().value)

    def parseExpression(self):
        left = self.parseParen()
        if(self.accept(Tok.OPERATOR)):
            op = Literal(self.getTok().value)
            self.nextTok()
            right = self.parseExpression()
            return BinaryExpression(left=left, operator=op, right=right)
        else:
            return left

    def parse(self):
        ast = []
        while(self.index < len(self.listOfTok)):
            ast.append(self.parseExpression())
            self.nextTok()
        return ast