#  We are making n stone piles! The first pile has n stones. 
# If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.

n = int(input("Number of piles n = "))
number_of_piles = range(0, n)  # add +1 to the desired number of piles (n). n is not included in range.
stones = n
print()
if n % 2 == 0:
    print("All piles have an even number of stones.")
else:
    print("All piles have an odd number of stones. ")
print()
stone = n
for i in number_of_piles:
    if n % 2 == 0:
        stones = 2 * 1 + n
        print(f"Pile number {i+1} has {stones} stones")
    else:
        stones = 2 * i + n
        print(f"Pile number {i+1} has {stones} stones")
