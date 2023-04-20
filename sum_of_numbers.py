print("Calculate the multiplication of all numbers from 1 to a given number")
x = int(input("Enter number "))
for i in range(1, x + 1):
    m = i * (i + 1)
print("The product is:", m)



# Multiply all the numbers in a list
list_of_numbers = [1, 3, 4, 5, 88, 15]
product = 1
for i in list_of_numbers:
    product = product * i
print(product)
