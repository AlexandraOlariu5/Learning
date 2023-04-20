# Write a Python program to find a list of integers with exactly two occurrences of nineteen 
# and at least three occurrences of five. Return True otherwise False. 



# print("Insert a random list of integers.")
# list1 = []
occurrences_of_nineteen = 0
occurrences_of_five = 0
element = ""
# list_of_int = input()
# for i in list_of_int:

#     list1.append(i)
# print(list1)


# while True: 
#     value = input()
#     if value == "":
#         break
#     list1.append(value)
# print(list1)

list2 = [5,6,7,5,19,19,5,8,1,32]
# for element in list2:
#     if element == 19:
#         occurrences_of_nineteen += 1

#         if occurrences_of_nineteen.count() == 2:
#             print("True")
#         else:
#             print("False")
#     elif element == 5:
#         occurrences_of_five += 1
#         if occurrences_of_five.count() >= 3:
#             print("True")
#         else:
#             print("False")
if list2.count(19) == 2 and list2.count(5) >= 3:
    print("True")
else:
    print("False")



