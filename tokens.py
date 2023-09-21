import enum

class Tok(enum.Enum):
    OPERATOR = 1
    NUMBER = 2
    LEFT_PAREN = 3
    RIGHT_PAREN = 4

class TokType:
    def __init__(self, type, value ):
        self.type = type
        self.value = value 

    def __repr__(self):
        return f"TokType(type:{self.type}, value:{self.value})"