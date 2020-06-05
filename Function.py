from Set import Set

class Function:

    def __init__(self, domain, codomain, f):
        domain = Set(domain)
        codomain = Set(codomain)
        self.domain = domain
        self.codomain = codomain
        self.f = f

    def __call__(self, element):
        if element not in self.domain:
            return "Element must be in domain!"
        return self.f(element)

    def image(self):
        return Set(self(element) for element in self.domain)

    def is_surjective(self):
        for i in self.codomain:
            if i not in self.image():
                return False
        return True

    def is_injective(self):
        return len(self.image()) == len(self.domain)

    def is_bijective(self):
        return self.is_surjective() and self.is_injective()
