from tokens import *
    
def lex(file):
    listOfTokens = []
    for w in file:
        if(w.isnumeric()):
            listOfTokens.append(TokType(Tok.NUMBER, int(w)))
        if(w == "+" or w == "-" or w == "/" or w == "*"):
            listOfTokens.append(TokType(Tok.OPERATOR, w))
        if(w == "("):
            listOfTokens.append(TokType(Tok.LEFT_PAREN, w))
        if(w == ")"):
            listOfTokens.append(TokType(Tok.RIGHT_PAREN, w))
        if(w == ";"):
            listOfTokens.append(TokType(Tok.SEMICOLON, w))
    return listOfTokens