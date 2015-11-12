'''
Created on 11 Nov 2015

@author: chris
'''
def main():
    a = RationalNumber(1, 2)
    b = RationalNumber(1, 3)
    print a + b
    print a - b
    print a*b
    print a/b

class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        
    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other) # not implemented
        
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 + d1*n2, d1*d2)
    
    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other) # not implemented
            
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)
    
    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other) # not implemented
           
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)
    
    def __div__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other) # not implemented
           
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2, n2*d1)        
        
    def __str__(self):
        return "%s/%s" % (self.n, self.d)
    
    __repr__ = __str__
    
if __name__ == '__main__':
    main()