from random import sample

class Set(set):

    def __mul__(self, other):
        if not isinstance(other, Set):
            other = Set(other)
        return Set(((a,b) for a in self for b in other))

    def pick_arbitrary(self):
        return sample(self, 1)

    def is_empty(self):
        return len(self) == 0

    def is_subset(self, other):
        for a in self:
            if a not in other:
                return False
        return True
