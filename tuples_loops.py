# Iterate through the items and print the values
thistuple = ("peach", "apricot", "sour cherry")
for x in thistuple:
  print(x)

print()
for i in range(len(thistuple)):
  print(thistuple[i])
print()

# Looping through the tuple items by using a while loop.
i = 0
while i < len(thistuple):  # determine the length of the tuple
  print(thistuple[i])
  i = i + 1

print()
tuple_for_taste = ("sour", "sweet", "bitter", "sweet", "sweet")
print("'sweet' occurs for : ", tuple_for_taste.count("sweet"), "times")
