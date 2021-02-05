############################################################
#
#  Jack Schneiderhan
#
#  CS115-B/C HW1 ~ Applications of Map & Reduce
#
#  Due : Sep. 20th, 2019
#
#  Pledge : I pledge my honor that I have abided by the Stevens Honor System.
# 
############################################################


# All functions should be written using map/reduce.
# No loops, no recursion, or other built-in functions unless explicitly allowed.
# You are free to write helper functions, so long as the main functions work as intended.

from functools import reduce
from math import factorial, sqrt # this import is necessary to use sqrt and factorial.

def taylorApproxE(lastIter):
    '''compute an approximation of e using
       the taylor series of e^x (around 0) when x=1'''
    
    L = range(lastIter + 1)
    
    def taylor(n):
        return 1 / factorial(n)
    
    def listMake(L):
        return map(taylor, L)

    def add(x, y):
        return x + y
    
    return reduce(add,listMake(L))

def vectorNorm(vect1):
    '''compute the vector norm of a list,
       a.k.a. the square root of the sum of the squares
       of what is in the list'''
    
    def squareIt(n):
        return n**2
    
    def add(x, y):
        return x + y

    def listMake(L):
       return map(squareIt, L)

    return sqrt(reduce(add, listMake(vect1)))

def arithMean(vect1):
    '''computes the arithmetic mean of a list of numbers'''

    def makeMean(n):
        return n / len(vect1)
    
    def add(x, y):
        return x + y

    def listMake(L):
        return map(makeMean, L)

    return reduce(add, listMake(vect1))



