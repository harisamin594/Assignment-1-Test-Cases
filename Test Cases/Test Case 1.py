#Test Case 1

import doctest

def square(x):

    """

>>> square(2)
4

>>> square(5)
25

>>> square(7)
49

    """
    
    return x+x #here * is replaced with +, hence code becomes incorrect

doctest.testmod()
