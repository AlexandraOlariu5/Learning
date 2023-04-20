# Write a Python program that accepts a list of integers and calculates the length and the fifth element.
# Return true if the length of the list is 8 and the fifth element occurs twice in the said list.
list1 = [12, 1, 9, 34, 6, 7, 6, 12, 16, 777, 6, 56]
length = len(list1)
print(length)
fifth_el = list1[4]
fifth_el_occurence = 0
print(fifth_el)
print()
if length == 8:
    print("True")
else:
    print("False")
print()
for i in list1:
   if i == fifth_el:
       fifth_el_occurence += 1
       print(fifth_el_occurence)
       if fifth_el_occurence == 2:
           print("True")
       else:
           print("False")
