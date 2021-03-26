class Other(object):
    
    def override(self):
        print("other override()")

    def implicit(self):
        print("other implicit()")

    def altered(self):
        print("other altered()")

class Child(object):
    
    def __init__(self):
        self.buddy = Other()
    def implicit(self):
        self.buddy.implicit()
    def override(self):
        print("Child override()")
    def altered(self):
        self.buddy.altered()
        print("Child altered")

son = Child()
son.implicit()
son.override()
son.altered()

