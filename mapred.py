from functools import reduce

'''finds the longest string in the given list of strings'''
def findL(L):
    '''returns the string length along with the string itself
       parameter: a string'''
    def f(S):
        return [len(S), S]
    
    '''returns a list with the lengths of the strings
       parameter: a list of strings'''
    def listMake(L):
        return list(map(f, L))
    
    return reduce(max,listMake(L))



