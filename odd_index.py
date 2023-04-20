# Use a loop to display elements from a given list present at odd index positions
given_list = [11, 14, 22, 56, 2, 89, 31, 67, 54, 89, 77, 12, 5, 1, 7, 3, 12]
odd_index = []
for i in given_list[1::2]:
# two by two stepping from 1, to display values with odd index
    odd_index.append(i)
print(odd_index)

    