""" String Note
String is immutable or non-mutable. This means that items of the string can't be changed.

Functions can be called only by its name, as it is defined independently.
But methods can't be called by its name only, we need to invoke the class by a reference of that class in which it is
defined, i.e. method is defined within a class and hence they are dependent on that class.

Simple
    - how to use '
    - get a character of the string
    - string object does not support item assigment.
Function:
    - len()
Method:
    - find()
"""
""" 
Simple
"""
# ? how to use '
s = 'Even\'s'  # or, s = "Even's"
print(s)  # output: Even's

# ? get a character of the string
country = "Bangladesh"
print(country[0])  # output: 'B'
print(country[1])   # output: 'a'
print(country[2])   # output: 'n'
print(country[6])   # output: 'd'
print(country[8])   # output: 's'
print(country[9])  # output: 'h'
try:
    print(country[10])   # ! output: IndexError: string index out of range.
except IndexError:
    print("IndexError: string index out of range.")

# ? string object does not support item assigment
country = "Bangladesh"
try:
    country[0] = "b"   # ! output: TypeError: 'str' object does not support item assignment.
except TypeError:
    print("TypeError: 'str' object does not support item assignment.")

"""
Method
"""
""" len()
    - Return the length [total character count] of the string.
        s = "hello"
        len(s)
    return: 5
"""
print("len():\n", len.__doc__)

s = "hello"
print(len(s))

""" find()
    - Return the lowest index in S where substring sub is found.
"""
print("find():\n", s.find.__doc__)
