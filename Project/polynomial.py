'''
>>> a = GP(4)
>>> f = Polynomial(4, a)
>>> print(f.__repr__())
0+1x^1+2x^2+3x^3

>>> b = GP(4)
>>> g = Polynomial(4,a)
>>> print(g.__repr__())
0+1x^1+2x^2+3x^3

>>> print(f.add(g))
0+2x^1+0x^2+2x^3
'''


from Group import GP
# import random

class Polynomial:
    def __init__(self, power: int, coefficient: GP) -> None:
        self.power = power
        self.c = coefficient
        self.coe = [0]*power
        for i in range(power):
            # if we want to generate random polynomials, we can use the following
            # self.coe[i] = (random.choice(coefficient.value))
            # but for now, let's stick with the same coefficients
            self.coe[i] = self.c.value[i]
        self.var = 'x'
    
    # accessor, return the whole polynomial in string 
    def __repr__(self):
        self.output = [0]*self.power
        for i in range(self.power):
            if i == 0:
                self.output[i] = self.coe[i]
            else:
                self.output[i] = str(self.coe[i]) + self.var + '^' + str(i)
        self.realout = ''
        for i in self.output:
            self.realout += str(i)
            self.realout += '+'
        return self.realout[:-1]

    # add two polynomials together, while making sure the coefficients are in the equivalent class
    def add(self, other):
        assert self.c.compare(other.c)
        for i in range(self.power):
            self.coe[i] += other.coe[i]
            self.coe[i] = self.c.equivclass(self.coe[i])
        return self.__repr__()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")