# list examples(Here we get index out of bound if we use the index greater than  the size of the list)
colors = ['red', 1, 'green', 'pink', 'purple']
print(colors[1])
print(len(colors))
# print(colors[7]) // we get index out of bounds error

# Slicing Lists(Here we don't get index out of bound if we use the index greater than  the size of the list)
my_list = [1, 2, 3, 4, 5]
print(my_list[0:3])
print(my_list[1:4:2])
new_list = my_list[1:3]
print(new_list)

list_colors = ['red', 'blue', 'green', 'pink', 'purple']
print(list_colors[1:4])

# add and remove elements
list1 = [7, 5, 8, 3, 9, 10]
list1.append(12)  # append adds the given value at the end of the list
list1.insert(4, 13)  # adds the value at the mentioned index , here 4 is index and 13 is the value in that index
list1.remove(9)  # removes the value mentioned in the remove function
list1.pop()  # removes the last element
list1.pop(5)  # pops out the value in the given index
# print(list1.sort()) gives an error
list1.sort()  # sorts the values in the ascending order
print(list1)

list_colors1 = ['red', 'blue', 'green', 'pink', 'purple']
list_colors1.pop(0)
list_colors1.remove('purple')
list_colors1.append('white')
print(list_colors1)

# Nested List
nested_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(len(nested_list))
print(len(nested_list[2]))
print(nested_list[2][1])
print(nested_list[2])

#  extend(), this method is used to add multiple elements at the same time at the end of the list.
list1.extend([17, 'Akhila', 'Sirikonda'])
print(list1)

List = [1, 2, 'Akhila', 4, 'Sirikonda', 6, 'Divya']

# accessing an element using negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])

# Printing elements from beginning till end
sliced_list = List[:]
print(sliced_list)

Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

cars = ["Ford", "Volvo", "Volvo", "BMW"]

print(cars.count("Volvo"))

print(cars.reverse())  # returns None
print(cars)

print(cars.reverse())  # returns None
print(cars)  # ['BMW', 'Ford', 'Volvo', 'Volvo']
