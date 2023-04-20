# Sets are used to store multiple items in a single variable. 
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

first_set = {"tulip", "dahlia", "peony", "tulip"}

print(first_set)  # the duplication will be ignored

another_set = {1, 2, 3, True, False}  # 1 and True are treated as duplicates
print(another_set)
print()

# Access the set with for 
for x in first_set:
    print(x)
print()
print("margaret" in first_set)
# Once a set is created, you cannot change its items, but you can add new items.
if "tulip" in first_set:
    first_set.add("rose")
print(first_set)
# Mind that the items don't appear in a determined order.

print()
autumn_flowers = {"aster", "chrysanthemum", "crocus"}
first_set.update(autumn_flowers)
print(first_set)
print()

# Removing items
autumn_flowers.remove("aster")
print("Remove 'aster: '", autumn_flowers)
# if the items doesn't exist => Error

# using the discard() method !=> Error
autumn_flowers.discard("daffodil")
print("There's no 'daffodil'", autumn_flowers)
print()
# remove a random item:
flower = autumn_flowers.pop()
print(flower)
print(autumn_flowers)
print()

# Joining, by creating a new set
european_flowers = autumn_flowers.union(first_set)
print(european_flowers)
print()

# keep the common elements
set1 = {1, 2, 3, 4, 5, 7, 8}
set2 = {True, 2, 3, 6, 5}
set1.intersection_update(set2)
print(set1)
print()

# Keep All, But NOT the Duplicates
set1.symmetric_difference_update(set2)
print(set1)  # returns the differents items from the first set
print()

difference = set1.symmetric_difference(set2)
# return all the items fro both sets with no duplicate
print(difference)
print()

# Check two sets have a intersection or not
new_set = {"ab", "cd", "rb", "acc", "ok"}
another_new_set = {"ww", "xy", "fg", "ok", "ab"}
check = new_set.isdisjoint(another_new_set)
print(check)
# returns True if none of the items are present in both sets, otherwise it returns False.




