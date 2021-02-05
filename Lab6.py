##Jack Schneiderhan
##I pledge my honor that I have abided by the Stevens Honor System.
##10/4/19

def decimalToBinary(x):
    '''returns the binary form of the integer number provided'''
    if(x == 1):
        return [1]
    elif(x%2 == 0):
        return [0] + decimalToBinary(x//2)
    else:
        return [1] + decimalToBinary(x//2)

def binaryToDecimal(num):
    '''returns the integer form of the binary number provided'''
    if(len(num) == 0):
       return 0
    elif(num[-1] == 0):
        return binaryToDecimal(num[:-1])
    else:
        return 2**(len(num) - 1) + binaryToDecimal(num[:-1])
        
def incrementBinary(num):
    '''given a binary num, return a binary num that is one larger'''
    return incrementHelper(num, 1)
    
def incrementHelper(num, carry):
    '''helper function for the incrementBinary method'''
    if num == []:
        if carry == 1:
            return num + [carry]
        else:
            return []
    elif num[0] + carry > 1:
        return [0] + incrementHelper(num[1:], 1)
    elif num[0] + carry == 1:
        return [1] + incrementHelper(num[1:],0)
    else:
        if num[-1] == 0:
            return num[0:-1]
        return num
    
def addBinary(num1, num2):
    '''adds two binary numbers together'''
    if (len(num1) < len(num2)):
        length = len(num2) - len(num1)
        num1 = num1 + ([0] * length)
    elif(len(num2) < len(num1)):
        length = len(num1) - len(num2)
        num2 = num2 + ([0] * length)

    return addHelper(num1, num2, 0)

def addHelper(n1, n2, carry):
    '''helper function for the addBinary method'''
    if n1==[] or n2==[]:
        if carry == 0:
            return []
        else:
            return [carry]

    add = n1[0] + n2[0] + carry

    if add == 0:
        return [0] + addHelper(n1[1:], n2[1:], 0)
    if add == 1:
        return [1] + addHelper(n1[1:], n2[1:], 0)
    if add == 2:
        return [0] + addHelper(n1[1:], n2[1:], 1)
    if add == 3:
        return [1] + addHelper(n1[1:], n2[1:], 1)

    
    
