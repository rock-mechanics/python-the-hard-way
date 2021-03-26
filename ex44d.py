class Parent(object):
    
    def override(self):
        print("Parent overide()")
    
    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        super().altered()
        print("Child altered()")

dad = Parent()
son = Child()

dad.implicit()
dad.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
