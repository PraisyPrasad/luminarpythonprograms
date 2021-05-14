class Parent:
    parent_name = 'Arun'

    def m1(self, age):
        self.age = age
        print("my name is", Parent.parent_name)
        print(self.age)
class Mobile:
    def mob(self):
        print("i have 1+")


class Child(Parent,Mobile):
    def m2(self, cage):
        self.cage = cage
        print("parent name is", Parent.parent_name)
        print(self.age)
        print(self.cage)


c = Child()
c.m1(23)
c.m2(12)
c.mob()