# Write a program to display all prime numbers within a range

x = int(input("Choose a limit for your range "))
list_of_primes = []
for number in range(1, x + 1):
# all prime numbers are greater and different than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            list_of_primes.append(number)
print(list_of_primes)


