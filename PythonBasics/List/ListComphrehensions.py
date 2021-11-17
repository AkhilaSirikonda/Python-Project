# Python program to demonstrate list
# comprehension in Python
# List comprehension is an elegant way to define and create a list in python.
# We can create lists just like mathematical statements and in one line only.

# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []

for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)

print(odd_square)

# A list comprehension generally consist of these parts :
# 1.Output expression,
# 2.Input sequence,
# 3.A variable representing a member of the input sequence and
# 4.An optional predicate part.
"""
lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
"""

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print('\nprime numbers between 1 to 50 is:')
print(primes)

# list for lowering the characters
print([x.lower() for x in ["A", "B", "C"]])

# list which extracts number
string = "my phone number is : 11122 !!"

print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print(numbers)

# A list of list for multiplication table
a = int(input("enter the input for multiplication:"))
table = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
    print(i)

lst = list(range(1, 11))
print(lst)
print(lst[::-1])  # prints in reverse

# We can use filter function to filter a list based on some condition
# Provided as a lambda expression as first argument and list as second argument,
# example of which is shown below :

import functools

#  filtering odd numbers
lst = filter(lambda x: x % 2 == 1, range(1, 20))
print("filtering odd numbers")
print(list(lst))

#  filtering odd square which are divisible by 5
lst = filter(lambda x: x % 5 == 0,
             [x ** 2 for x in range(1, 11) if x % 2 == 1])
print("filtering odd square which are divisible by 5")
print(list(lst))

#   filtering negative numbers
lst = filter((lambda x: x < 0), range(-5, 5))
print("filtering negative numbers")
print(list(lst))

#  implementing max() function, using
print("implementing max() function, using lambda")
print(functools.reduce(lambda a, b: a if (a > b) else b, [7, 12, 45, 100, 15]))

# splitting
fruits = "Banana, Apple, Orange"
print(fruits)
print("After Splitting:")
print(fruits.split(','))

d = "1 2 4"
a,b,c = d.split()
print(a,b,c)



