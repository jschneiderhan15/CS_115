#Jack Schneiderhan
#I pledge my honor that I have abided by the Stevens Honor System.

def dotProduct(L, K):
    '''output the dot products of the lists L and K'''
    if L == [] or K == []:
        return 0.0
    else:
        return L[0] * K[0] + dotProduct(L[1:], K[1:])

def expand(S):
    '''expand the string S into a list of characters'''
    L = []
    if S == "":
        return []
    else:
        L += S[0]
        L += expand(S[1:])
    return L
        
def deepMember(e, L):
    '''tests if the element e is anywhere in list L'''
    if L == []:
        return False
    if isinstance(L[0], list):
        if e == L[0][0]:
            return True
        else:
            return deepMember(e, L[0][1:])
    else:
        if e == L[0]:
            return True
        else:
             return deepMember(e, L[1:])

             
def removeAll(e, L):
    '''removes all elements e from list L'''
    K = []
    if L == []:
        return K
    else:
        if e == L[0]:
            K = [L[1]] + removeAll(e, L[2:])
            return K
        else:
            K = [L[0]] + removeAll(e, L[1:])
            return K
        
def deepReverse(L):
    '''reverses the list given, along with any lists imbedded within the list'''
    if L == []:
        return L
    elif isinstance(L[0], list):
        return 0
    else:
        return deepReverse(L[1:]) + [L[0]]
   
        
        
