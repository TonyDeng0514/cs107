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
