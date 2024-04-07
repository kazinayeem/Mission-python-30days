# day 13
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Define a subclass inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Another subclass inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Test the speak method of each object
print(dog.name + " says:", dog.speak())
print(cat.name + " says:", cat.speak())
