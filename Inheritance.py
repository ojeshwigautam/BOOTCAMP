Inheritance:
Definition: Inheritance is a mechanism in object-oriented programming where a new class inherits properties and behaviors (methods) from an existing class. The existing class is called the base class or superclass, and the new class is called the derived class or subclass.
Example:

# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()
dog.speak()  # Inherited method from Animal class
dog.bark()   # Method specific to Dog class
Exception Handling:
Definition: Exception handling is a way to deal with errors that occur during program execution. It involves identifying, catching, and handling exceptions gracefully so that the program doesn't crash unexpectedly.
Example:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division performed successfully.")
finally:
    print("End of program.")

We attempt to perform division but anticipate potential errors such as invalid input or division by zero.
try block contains the code that might raise an exception.
except blocks catch specific types of exceptions and handle them accordingly.
else block executes if no exception occurs.
finally block executes regardless of whether an exception occurred or not, useful for cleanup tasks.
