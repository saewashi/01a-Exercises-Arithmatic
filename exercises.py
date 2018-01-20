'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python.
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening.


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15
#25
8 - 1
# 7 This is a subtraction operator, which is producing the result of subtracting two numbers from each other.
10 * 2
# 20. This is a multiplication operator, which is multiplying two numbers together, to get the ending result.
35 / 5
# 7.0 This is a division operator, which is dividing two numbers together, to get the ending result.

35 / 4
# 8.75
35 // 4
# 8. This is taking the remaining decimals from the ending result
# What is the difference between the / operator and the // operator?
# The difference between the / operator and the // operator is that the / divides the number, wheras // still divides, but gets rid of the remaining decimals at the end.

2 ** 5
# 32
# What does the ** operator do?
# The ** operator is like the multiplication operator, but it is performing a exponent operation, by taking 2 and rising it to the 5th power.
# For example: 5 ** 10 = 9765625
5 % 3
# 2
5 % 2
# 1
5 % 4
# 1
# What does the % operator do?
# This is performing floor division, which is dividing the two numbers, but taking the remainder.

(1 + 3) * 2
# 8
# What effect do the parenthesis have on this statement?
# The parenthesis are a part of mathematical operation, called PEMDAS, which is -
# Parenthesis, Exponents, Multiplication, Division, Addition, and Subtraction.
# Since you have to follow that form, whatever is in the parenthesis calculated first, and then so on.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>, this is a data type that produces an integer
type(3.0)
# <class 'float'>, this is a data type that produces a result that was  either too big or too small to be represented by an integer.
type("word")
#<class 'str'>, this is a data type that produces a String
type(True)
# <class 'bool'>, this is a Boolean that checks to see if the result is true
type(False)
# <class 'bool'>, this is a Boolean that checks to see if the result is false
type(None)
# <class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another.
int(3.0)
# 3
float(7)
# 7.0
str(55)
# '55'
bool(1)
# True
# How can you tell the difference between these four different types?
# How you can tell the difference between these four different types of data, is knowing what produces what.
# A boolean data type is going to check if something is true or false, a String data type will produce a string of words, -
# a float data type will produce something that is too big or too small to be represented by an integer, -
# and an integer data type will produce an integer.

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# The + operator adds both the strings together to produce the result: 'Hello world!'

"This is a string"[0]
# 'T'
"This is a string"[5]
# 'i'
"This is a string"[8]
# 'a'
# What is happening as you change the number?
# What is happening is that each number is representing a letter within the string, and is printing it out as a result.
# For exmaple:  "This is a string"[1] = 'h'

"This is a string"[-1]
# 'g'
# What happens when you use a negative number?
# What happens when a negative number is used, is that it is going backwards of the string,-
# so it is finding the letter that is represented by the negative number in the string.

"%s can be %s" % ("strings", "interpolated")
# What is happening here?
# What is happening here, is that 'can be' is being interpolated between the two strings, like the result:
# 'strings can be interpolated'


# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# This is only producing 'What is your name?'
# What just happened?
# I'm guessing what was supposed to happen, is that the code or the input method is asking the user for their name, and the user puts in there name, -
# and then it produces the result 'Hello, (name)', whatever name the user inputs.

# For your next assignment, you will need to use random numbers
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# Random is being imported, along with randint,, shuffle, and sample.

randint(1,100)
# How is this different?
# This is producing a random integer, which resulted in 49, which is different because it is randomizing the integers.

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# What is happening is that shuffle is supposed to shuffle the items in the list, and produce the randomized items.

print(sample(items, 1))
# What does this do?
# What this is doing is grabbing a sample out of the list, grabing one number of out the list, which produced 7.

print(sample(items, 5))
# What does the second parameter control?
# What this is doing, is producing a sample list of 5 numbers, which is: [3, 6, 8, 5, 0]

for i in range(0,5):
	print(i)
# 0
# 1
# 2
# 3
# 4

# What is happening here? What happens if you change the two range parameters?
# What is happening here, is that this code is producing a range from 0 to 5, starting from 0, and produces that list.
# If it were to change, then it would produce a different number list depending the ranges to pick from.
