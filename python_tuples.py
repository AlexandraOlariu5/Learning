# Tuples are used to store multiple items in a single variable.
# They are a collection that can't be changed
# They are ordered, indexed, allowing duplicates

thistuple = ("apple",)  # to create a tuple with one item,
# you MUST add a comma after your item, unless it won't be
# recognised by python
print(type(thistuple))

tuple1 = ("aubergine", "spinach", "lentils")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, "Malibu", 12)
print(tuple1)
print(tuple2)
print(tuple3)

x = ("pink", "red", "blue")
y = list(x)  # convert tuple to list for changes
y[1] = "purple"   # replace an item on position 1
x = tuple(y)  # convert back to a tuple

print(x)
print()

# Adding items - there's no built-in functions for this 
# We use convertion
sports_tuple = ("rugby", "footbal", "golf", "tenis")
sports = list(sports_tuple)
sports.append("swimming")
print(tuple(sports))

print()

# You can add a tuple to another tuple
new_tuple = (1, 2, 3, False)
another_tuple = (4, 5, 6, True)
print(new_tuple + another_tuple)

print()

# Removing an item, by converting the tuple to a list
new_list = list(new_tuple)
print(new_list)
new_list.remove(3)
print(new_list)

print()
# unpacking a tuple = extracting values back into variables
 
names_tuple = ("Arthur", "Harry", "John", "Katherine")
(Emilly, Charlie, Sunita, Mike) = names_tuple
print(Emilly)
print(Charlie)
print(Sunita)
print(Mike)
print()

# If the number of variables is less than the number of 
# values, you can add an * to the variable name and the 
# values will be assigned to the variable as a list:

clothes_tuple = ("dress", "blouse", "sweater", "trench", "coat")

(cotton, cashmere, *lace) = clothes_tuple

print(cotton)
print(cashmere)
print(lace)
