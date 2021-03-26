class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def altered(self):
        print("Child, before parent altered()")
        super().altered()
        print("Child altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
