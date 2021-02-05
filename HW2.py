'''
Name:Jack Schneiderhan

Date: 9/22/19

CS115 - HW 2 ~ Recursion

Pledge: I pledge my honor that I have abided by the Stevens Honors System.
'''

## Part 1 ~ Change

def makeChange(val, coins):
    '''returns the smallest number of coins it would take to make a given value,
    along with the values of the coins'''
    if val == 0:
        return [0,[]]
    elif coins == [] or val < 0 :
        return [float("inf"),[]]
    elif coins[0] > val:
        return makeChange(val, coins[1:])
    else:
        use = makeChange(val - coins[0], coins)
        coinList = [use[0] + 1, [coins[0]] + use[1]]
        lose = makeChange(val, coins[1:])
        if coinList[0] < lose[0]:
            return coinList
        return lose


## Part 2 ~ Least Common Substrings

def LCS(a, b): 
    '''returns the least common substring between two strings'''
    if (a == '' or b == ''):
        return ''
    elif (a[0] == b[0]):
        return a[0] + LCS(a[1:],b[1:])
    else:
        useIt = LCS(a[1:], b)
        loseIt = LCS(a, b[1:])
    if (len(useIt) < len(loseIt)):
        return loseIt
    elif(len(useIt) == len(loseIt)):
        return loseIt
    else:
        return useIt
            


def PLCS(a, b):
    '''returns the indexes of the longest common substrings between
    two strings'''
    commonString = LCS(a,b)
    if commonString == '':
        return [[-1], [-1]]
    else:
        return [helpPLCS(a, commonString, -1)] + [helpPLCS(b, commonString, -1)]

def helpPLCS(s1, s2, index):
    '''helper function for the PLCS method'''
    if(s1 == '') or (s2 == ''):
        return []
    elif (s1[0] == s2[0]):
        index += 1
        return [index] + helpPLCS(s1[1:], s2[1:], index)
    else:
        index+=1
        useIt = helpPLCS(s1[1:], s2, index)
        loseIt =  helpPLCS(s1[1:], s2, index)
    if(len(useIt) < len(loseIt)):
        return loseIt
    else:
        return useIt

    









