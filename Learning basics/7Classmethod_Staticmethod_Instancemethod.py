'''
A class method in Python is defined using the @classmethod decorator and takes cls as its first parameter, 
which refers to the class itself.
A static method in Python is defined using the @staticmethod decorator and does not take any special 
first parameter (neither self nor cls).
Both can be called with Class object or directly with class name
'''

# Class method - Mostly used for Factory design
class Person:
    @classmethod
    def get_class_name(cls):
        print(f"Class method called from {cls.__name__}")

Person.get_class_name()

# Static method - Mostly used for utility functions
class Utility:
    @staticmethod
    def welcome():
        print("Static method called")

Utility.welcome()

'''Property decorator Python'''
#https://www.geeksforgeeks.org/python-property-decorator-property/

'''
## What is an Instance Method?

An instance method is a function defined inside a class that operates on instance data (attributes). It automatically receives the instance as the first parameter (self).

**Key Characteristics:**
- Defined inside a class
- First parameter is always `self`
- Can access and modify instance attributes
- Called on an instance of the class
- Each instance has its own copy of the method
'''
class Car:
    """A simple car class with instance methods."""
    
    def __init__(self, brand, model, year):
        """Initialize car attributes."""
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self):
        """Instance method to increase speed."""
        self.speed += 10
        return f"{self.brand} {self.model} accelerated to {self.speed} mph"
    
    def brake(self):
        """Instance method to decrease speed."""
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0
        return f"{self.brand} {self.model} slowed down to {self.speed} mph"
    
    def get_info(self):
        """Instance method to get car information."""
        return f"{self.year} {self.brand} {self.model}, Speed: {self.speed} mph"


# Creating instances
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

# Calling instance methods
print(car1.accelerate())        # Toyota Camry accelerated to 10 mph
print(car1.accelerate())        # Toyota Camry accelerated to 20 mph
print(car1.brake())             # Toyota Camry slowed down to 10 mph
print(car1.get_info())          # 2023 Toyota Camry, Speed: 10 mph

print(car2.accelerate())        # Honda Civic accelerated to 10 mph
print(car2.get_info())          # 2022 Honda Civic, Speed: 10 mph

# Each instance maintains its own state
print(f"Car1 speed: {car1.speed}")  # Car1 speed: 10
print(f"Car2 speed: {car2.speed}")  # Car2 speed: 10
