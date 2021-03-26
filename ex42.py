# Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # Dog has-a attribute name
        self.name = name

# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a attribute name
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has-a attribute name
        self.name = name

        # Person has-a pet
        self.pet = None

# Employee is-a Person
class Empolyee(Person):
    def __init__(self, name, salary):
        # what is this strange magic
        super().__init__(name)
        # Empolyee has-a attribute salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is a Person
satan = Person("Satan")

# mary is a Person
mary = Person("Mary")

# mary has-a pet which is-a satan
mary.pet = satan

frank = Empolyee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
