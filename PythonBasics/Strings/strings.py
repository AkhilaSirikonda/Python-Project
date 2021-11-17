# strings
string = 'Akhila\'s'
string1 = '''Divya'''
print(string)
print(string1)

# strings concat
string2 = 'Sirikonda'
string3 = 8
result = 'Sirikonda Nagesh Uma, {s} {s1}'.format(s=string, s1=string1)
result1 = 'Sirikonda, {s} {s1}'.format(s1=string, s=string1)
resultString = f'{string2} has {string3} cousins'
print(resultString)
print(result)
print(result1)

# strings methods
# upper, lower, capitalize, endswith, isdigit are some of the functions used in string methods
birthday = 'may'
date = 23
birthday_gifts_phrase = f'{birthday} {date} is my birthdate'
birthday_gifts_phrase1 = 'my birthdate is {b} {d}'.format(b=birthday, d=date)
print((birthday_gifts_phrase))
print((birthday_gifts_phrase1))

# user input
college = input('enter your college name:')
id = input('enter your college id:')
print(f'Akhila from {college} with id {id}')

# input is used for strings type, in order to use it for other data types just type cast
gift1 = input('what do you want as your first gift:')
gift2 = input('what do you want as your second gift:')
bdy_gift = f'I got 2 gifts for my birthday 1:{gift1}'\
           f' and 2:{gift2}'
print(bdy_gift.upper())
