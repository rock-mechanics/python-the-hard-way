class Parent(object):
    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    def implicit(self):
        print("Child overide()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
