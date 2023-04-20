# The clasic version of creating a new list:
vegetables = ["lettuce", "beans", "onion", "buttercup", "baby corn", "asparagus"]
newlist = []  # containing only vegetables with 'b'
for i in vegetables:
    if i.startswith("b"):
        newlist.append(i)
print(newlist)


# Comprehension method:

newlist2 = [x for x in vegetables if x.startswith("l")]
print(newlist2)
