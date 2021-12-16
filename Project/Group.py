'''
Want to write a class that represents Z/nZ.
This is a group with modular addition.

>>> a = GP(2)
>>> a.expr()
[0, 1]

>>> b = GP(2)
>>> assert a.compare(b)
>>> assert not a.triv()
>>> c = GP(1)
>>> assert not a.compare(c)
>>> assert c.triv()
>>> c.expr()
[0]

>>> d = GP(0)
>>> d.expr()
The integers

>>> print(a.equivclass(2))
2

>>> e = GP(6)
>>> e.expr()
[0, 1, 2, 3, 4, 5]

>>> print(e.equivclass(7))
1
'''

class GP:
    def __init__(self, id: int) -> None:  # define the identity element when starting a new group
        assert type(id) == int    # since we are using integers here, the identity must be integers
        self.id = id    
        if self.id == 0:     # if 0 is the identity, this is the whole integers
            self.value = 'The integers'
        else:
            self.value = [i for i in range(self.id)]  # for any other number, the group will be integers until we reach identity.

    # accessor printing out all the element in the group
    def expr(self):
        print(self.value)

    # accessor, compare two groups
    def compare(self, other): 
        assert type(other) == GP
        if self.id == other.id:  # same identity implies every element is the same
            return True
        else:
            return False

    # accessor, determining if the group is trivial.
    def triv(self):  # trivial group is when the identity is 1, there would be only 1 element in the group which is the identity.
        if self.id == 1:
            return True
        else:
            return False
    
    # accessor, return the equivalent class of an element in this group
    def equivclass(self, input):
        assert type(input) == int
        if input == self.id:
            return self.id
        else:
            return input-(input % self.id)*self.id
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")