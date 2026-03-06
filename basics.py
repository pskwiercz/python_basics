import math
from os import name
########################################################
### Strings
########################################################
str = "Hello, World!"
print(str[0:5])
print(len(str))
print(str[0:-1]) # Hello, World
print(str[::2])  #str[start:stop:step]
print(str[::-1]) # reverse string
# copy string
str1 = str[:]
print(str1 + "\n\n")


capital = "Warsaw"
msg = f"The capital of Poland is {capital}"
print(msg + "\n\n")

########################################################
### Math https://docs.python.org/3/library/math.html
########################################################
print(round(2.3)) # 2
print(abs(-2.3)) # 2.3
print(pow(2, 3)) # 8
print(math.sqrt(16)) # 4
print(math.ceil(2.3)) # 3
print(math.floor(2.3)) # 2
print(math.log(10)) # 2.302585092994046
print(math.log10(10)) # 1

########################################################
### Lists
########################################################
list = [1, 2, 3, 4, 5]
print(list)
print(list[:]) # [1, 2, 3, 4, 5]
print(list[::2]) # [1, 3, 5]
print("\n\n")

list.pop() # remove last item
list.append(4) # add item to end
list.insert(0, 0) # add item to start
list.remove(0) # remove item
print(list.index(4)) # index of item
print(list.count(4)) # return number of occurrences of value
print(4 in list) # True
print(50 in list) # safer then index(50) because it will not return exception if item is not found
list.reverse() # reverse list
list.clear() # clear list
list2 = list.copy() # copy list
print("\n\n")

#2d list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0]) # [1, 2, 3]
print(matrix[0][0]) # 1
print(matrix[0][0:2]) # [1, 2]
print(matrix[0:2]) # [[1, 2, 3], [4, 5, 6]]
print(matrix[0:2][0:1]) # [[1, 2, 3]]


########################################################
### Tuples
########################################################
print("\n\nTuples")
tuple = (1, 2, 3)
print(tuple)
print(tuple[0]) # 1
print(tuple[0:2]) # (1, 2)
print(tuple[0:2][0:1]) # (1,)
print(tuple.index(3)) # index of item
print(tuple.count(3)) # return number of occurrences of value
print(3 in tuple) # True
print(50 in tuple) # safer then index(50) because it will not return exception if item is not found

#Unpacking
x, y, z = tuple # x = 1, y = 2, z = 3, same x = tuple[0] etc
print(z)

########################################################
### Dictionary
########################################################
print("Dictionary\n\n") # Key-value pair - key cannot be duplicated
customer = {
    "name": "John",
    "age": 30
}

print(customer["name"])
print(customer.get("name"))   

########################################################
### Methods
########################################################
print("\n\nMethods\n\n")

def user(name):
    print(f'Hello {name}')

user("John")

def user_param(name: name):
    print(f'hello {name}')

user_param(name="Anna")

########################################################
### Exceptions
########################################################
print("Exceptions\n\n")
try:
    age = int("30")
    x = age/0
except ValueError:
    print("Can't convert age")
except ZeroDivisionError:
    print("Can't divide by zero")

########################################################
### Classes
########################################################
print("Classes\n\n")

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def walk(self):
        print("Walk")

class Dog(Animal): # Inheritance
    def bark(self):
        print("Bark")

dog = Dog("Burek")
dog.walk()
dog.bark()


