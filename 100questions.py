# lambda
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

nums = [5, 2, 9]
sorted_nums = sorted(nums, key=lambda x: -x)
print(sorted_nums)

# Multi inheritance mro - method resolution order
class A:
    def say(self):
        print("A")

class B:
    def say(self):
        print("B")

class C(A, B):
    pass

c = C()
c.say()
print(C.mro())


# Monkey patching
import math
math.sqrt = lambda x: "No square roots allowed"
print(math.sqrt(9))  # Outputs: No square roots allowed

# __name i private field
class Person:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

person = Person("John")
print(person.getName())
person.name = "Adam"
print(person.getName()) # John

# Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

dog = Dog()
dog.make_sound()

# List comprehension
squares = [x*x for x in range(5)]
print(squares)

# Higher-order functions
def apply_twice(func, value):
    return func(func(value))

def square(x):
    return x * x
print(apply_twice(square, 2)) # 16

# Decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")
    
greet()

# Counter
from collections import Counter
c = Counter("banana")
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
print(c.most_common(1))
print(list(c.elements()))

# zip()
names = ['Alice', 'Bob']
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# recursive lambda
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5)) # 120

print(dir([]))