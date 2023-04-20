# Write a Python program that accepts an integer and determines 
# whether it is greater than 4^4 and which is 4 mod 34.
integer = int(input("Please enter a random integer: "))
if integer > 4 ** 4:
    print("True")
else:
    print("False")
if integer % 34 == 4:
    print("True")
else:
    print("False")
    print(integer % 34)
    