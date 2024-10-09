def checkTypeNotNumeric(*args):
    outPut = True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True
        
        
def addAllNos(*args):
    s = 0
    for x in args:
        s += x
    return s


myName = "Module utilities"
