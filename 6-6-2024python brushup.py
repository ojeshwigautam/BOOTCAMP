Input Statement (input()): This function allows a program to accept input from the user through the keyboard. It returns a string containing the user's input.

name = input("Enter your name: ")
print("Hello,", name)


Output Statement (print()): This function is used to display output to the user. It can print strings, numbers, variables, and expressions to the console.
Example

print("Hello, World!")


Data Types: Python supports various data types such as integers, floats, strings, lists, tuples, dictionaries, etc., which are used to store different kinds of data.
Example:
# Integer
x = 10

# Float
y = 3.14

# String
name = "Alice"

# List
numbers = [1, 2, 3, 4, 5]

# Tuple
coordinates = (10, 20)

# Dictionary
person = {"name": "Bob", "age": 30}


Expressions and Operators: Expressions are combinations of values and operators that produce a result. Operators are symbols that perform operations on variables and values.
Example:

# Arithmetic operators
result = 10 + 5 * 2

# Comparison operators
is_equal = (10 == 5)

# Logical operators
is_true = (True and False)


Type Casting: Type casting refers to the process of converting one data type to another.
Example:

# Integer to string
x = 10
x_str = str(x)

# String to integer
y_str = "20"
y = int(y_str)


Conditional Statements (if, elif, else): Conditional statements are used to perform different actions based on different conditions.
Example:

x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


Looping Statements (for, while): Looping statements are used to execute a block of code repeatedly.
Example:
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1


Jump Statements (break, continue): Jump statements alter the flow of a loop. break is used to exit the loop, while continue is used to skip the current iteration and continue with the next one.
Example:

# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)


1.Functions: Functions in Python are blocks of reusable code that perform a specific task. They are defined using the `def` keyword followed by the function name and parentheses.

Example:
def greet():
    print("Hello, World!")

greet()  # Call the function

2. Syntax of a Function:
   - def: Keyword to define a function.
   - Function Name: Name of the function.
   - Parameters (Optional): Variables passed to the function.
   - Colon :: Indicates the beginning of the function block.
   - Indentation: Body of the function.
   - Return Statement (Optional): Returns a value from the function.

Example:

def add(x, y):
    return x + y

3. Parameters: Parameters are placeholders for data that a function can accept. There are different types of parameters:
   - Positional Parameters: Defined in the function header by their position.
   - Keyword Parameters: Identified by their parameter name.
   - Default Parameters: Have default values assigned.
   - Variable Length Parameters (args, kwargs): Accept any number of arguments.

Example:
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")


4. Passing Functions as Arguments: In Python, functions can be passed as arguments to other functions.

Example:

def square(x):
    return x * x

def apply(func, x):
    return func(x)

result = apply(square, 5)
print(result)

5.Lambda Functions: Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of parameters but only one expression.

Example:
add = lambda x, y: x + y
result = add(3, 5)
print(result)







