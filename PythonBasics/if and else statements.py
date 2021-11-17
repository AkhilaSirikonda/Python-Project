"""
flow control
"""

"""
if statements
if condition:
 # block of code to be executed if the condition is true
"""
x = 23
if x == 100:
    print('x is 100')
print('x is not equal to 100')
if x <= 100:
    print(f'x is {x}')
if x > 100:
    print('x is greater than 100')

"""
else statements
if condition:
 # block of code to be executed if the condition is true
else condition:
 # block of code to be executed if the condition is false
"""
hour = 13
if hour >= 12:
    message = 'Good Afternoon Akhila'
else : message = 'Good Morning'
print(message)

"""
elIf statements
if condition1:
 # block of code to be executed if the condition1 is true
elif condition2:
 # block of code to be executed if the condition1 is false and condition2 is true
else condition3:
 # block of code to be executed if the condition1 is false, condition2 is false and condition3 is true
"""
hour = 19
name = 'Akhila'
if hour < 12:
    message = f'Good Morning {name}'
elif hour >= 12 and hour < 18:
    message = f'Good Afternoon'
else:
    message = f'Good Night {name}'
print(message)

# input function is used for integers so in order to take integer inputs just typecast the input with 'int' keyword
grade = int(input('enter your score between 1 and 100 :'))
if grade >= 90:
    print('A')
elif grade >= 80 and grade < 90:
    print('B')
elif grade >= 70 and grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
else:
    print('F')
