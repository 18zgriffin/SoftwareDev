
class Dog:
    kind  = 'Canine' #Class variable shared by all copies
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
d.add_trick("BackFlip")
d.add_trick("FrontRoll")
e = Dog('Buddy')
e.add_trick("sit")
e.add_trick("stand")

#print(e)
print(e.name)
print(e.kind)
print(e.tricks)
#print(d)
print(d.name)
print(d.kind)
print(d.tricks)

class Cat:
    kind  = 'Feline' #Class variable shared by all copies
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

f = Cat('Shit')
f.add_trick("Nothing")
f.add_trick("Meow")
g = Cat('Other')
g.add_trick("Poop")
g.add_trick("Scratch")

#print(f)
print(f.name)
print(f.kind)
print(f.tricks)
#print(g)
print(g.name)
print(g.kind)
print(g.tricks)