import random

class Set:

    def __init__(self, _set):
        _set = set(_set)
        self.set = _set

    def __repr__(self):
        return str({a for a in self.items()})

    def __len__(self):
        return len(self.items())

    def items(self):
        return self.set

    def cartesian_product(self, other):
        if not isinstance(other, Set):
            other = Set(other)
        return Set((a, b) for a in self.items() for b in other.items())

    def pick_arbitrary(self):
        return random.choice(self.items())

    def is_empty(self):
        return len(self.items()) == 0

    def is_subset(self, other):
        for a in self.items():
            if a not in other.items():
                return False
        return True
