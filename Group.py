from Set import Set
from Function import Function

class Group:

    def __init__(self, G, bin_op):
        if not isinstance(G, Set):
            raise TypeError("G must be a set!")
        if not isinstance(bin_op, Function):
            raise TypeError("Binary operation must be a function!")
        self.bin_op = bin_op
        self.G = G
