class Animals(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        print("{name} is running.".format(name=self.name))


class Mankind(Animals):

    def thinking(self):
        print("{name} is thinking.".format(name=self.name))


class Cat(Animals):

    def spoiled(self):
        print("The {name} is spoiled.".format(name=self.name))


class SuperCat(Mankind, Cat):

    def attractive(self):
        print("Every girls love {name}.".format(name=self.name))


s_c1 = SuperCat('Bridi', 8)
s_c1.action()
