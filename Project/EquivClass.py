'''
This is for practice and ideas only.
Since JD is always asking us to submit work on our scratch paper, this is my scratch paper file.
Nothing much happened here.

Feel free to ignore this file.
'''


from Group import GP

class Eqint:
    def __init__(self, seq: GP) -> None:
        self.value = seq.value

    def display(self):
        output = str(len(self.value))
        return output

    def equals(self, other):
        assert type(other) == Eqint
        if self.display() == other.display():
            return True
        else:
            return False

    def add(self, other):
        assert type(other) == Eqint
        self.value += other.value
