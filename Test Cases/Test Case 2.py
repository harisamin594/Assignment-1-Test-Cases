#Test Case 2

import doctest

def word_len(word):

    """
>>> word_len("haris")
5

>>> word_len("quality assurance")
17

>>> word_len("f.c.college")
11
    """
    count = 0
    
    for letter in word:
        count -= 1 #here + is replaced with - so the code becomes incorrect
    
    return count

doctest.testmod()
