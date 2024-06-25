

1. OOP (Object-Oriented Programming):
   - Object-Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields (attributes or properties), and code, in the form of procedures .

2. Class:
   - A class is a blueprint for creating objects (instances), providing initial values for state (member variables or attributes) and implementations of behavior (member functions or methods).

   python
   class Car:
       pass  # Placeholder for class definition
   

3. Objects:
   - An object is an instance of a class. It is a real-world entity that has state and behavior.

   ```python
   my_car = Car()  # Creating an object of the class Car
   

4. data Members:
   - Data members are variables that are associated with a specific class. They represent the state of an object.

   ```python
   class Car:
       def __init__(self, brand):
           self.brand = brand  # brand is a data member
   ```

5. Class Methods:
   - Class methods are functions that are bound to the class rather than the instance of the class.

   python
   class Car:
       @classmethod
       def show_info(cls):
           print("This is a car class")
   

6. Class Constructor and Destructor Methods:
   - Constructor (init) method is used for initializing newly created objects.
   - Destructor (del) method is used to perform cleanup actions when an object is no longer needed.

  
   class Car:
       def __init__(self, brand):
           self.brand = brand

       def __del__(self):
           print("Car object deleted")
  

7. Arguments:
   - Arguments are values passed to a function or method when called.


   class Car:
       def __init__(self, brand):
           self.brand = brand

       def display_info(self):
           print("Brand:", self.brand)

   my_car = Car("Toyota")
   my_car.display_info()  # Output: Brand: Toyota
   

8. Data Encapsulation:
   - Data Encapsulation is the bundling of data and methods that operate on that data into a single unit (class).

9. Data Abstraction:
   - Data Abstraction is the process of hiding the complex implementation details and showing only the essential features of the object.

10. Data Hiding:
    - Data Hiding is an OOP concept where the data is hidden within the class and can only be accessed through the class's methods.

Types of Data Hiding:
- Private Access Modifier**: Denoted by double underscore (__). Members are accessible only within the class.
- Protected Access Modifier**: Denoted by single underscore (_). Members are accessible within the class and its subclasses.
- Public Access Modifier**: No underscore. Members are accessible from outside the class.

Example:

class Car:
    def __init__(self):
        self.__speed = 0  # Private attribute

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed

my_car = Car()
my_car.accelerate()
print(my_car.get_speed())  # Output: 10
# print(my_car.__speed)  # Error: AttributeError: 'Car' object has no attribute '__speed'
