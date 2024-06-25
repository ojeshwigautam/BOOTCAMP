Lists:
Lists are ordered collections in Python that can contain elements of different data types.

my_list = [1, 2, 3]

try:
    print(my_list[3])  # Trying to access an index out of range
except IndexError:
    print("Index out of range")


Tuples:
Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.

my_tuple = (1, 2, 3)

try:
    my_tuple[0] = 4  # Trying to modify a tuple
except TypeError:
    print("Tuples are immutable")


Dictionaries:
Dictionaries are unordered collections of key-value pairs in Python.

my_dict = {'a': 1, 'b': 2}

try:
    print(my_dict['c'])  # Trying to access a key that doesn't exist
except KeyError:
    print("Key not found")


Sets:
Sets are unordered collections of unique elements in Python.

my_set = {1, 2, 3}

try:
    my_set.remove(4)  # Trying to remove an element that doesn't exist
except KeyError:
    print("Element not found")
