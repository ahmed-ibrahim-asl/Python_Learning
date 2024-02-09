'''
Derived from Greek word "Poly" means "many" and "morph" means "forms".
think of it as "Ability of single interface or method to take on
multiple forms " 

'''

# Example
class Animal:
    def speak(self):
        pass  # Abstract method


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Tweet!"


# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.speak())


# Create instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Demonstrate polymorphism
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Tweet!
