import numpy as np
import random

class Set(_set):
    def __init__(self, _set):
        _set = set(_set)
        self.set = _set

    def cartesian_product(self, other):
        return Set((a, b) for a in self.set for b in other)

    def pick_arbitrary(self):
        return random.choice(self.set)
