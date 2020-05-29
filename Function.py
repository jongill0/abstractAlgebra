from Set import Set

class Function:

    def __init__(self, domain, codomain, f):
        if not isinstance(domain, Set):
            domain = Set(domain)
        if not isinstance(codomain, Set):
            codomain = Set(codomain)
        self.domain = domain
        self.codomain = codomain
        self.f = f

    def __call__(self, element):
        if element not in self.domain.items():
            return "Element must be in domain!"
        return self.f(element)

    def image(self):
        return Set(self(element) for element in self.domain.items())

    def is_surjective(self):
        for i in self.image().items():
            if i not in self.codomain.items():
                return False
        return True

    def is_injective(self):
        return len(self.image()) == len(self.domain)

    def is_bijective(self):
        return self.is_surjective() and self.is_injective()

a = Set([i for i in range(10)])
b = Set([i for i in range(10)])
def f(x):return x
c = Function(a, b, f)
print(c.domain)
print(c.is_bijective())
