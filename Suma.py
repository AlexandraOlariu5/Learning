# Write a program to find a way of paying a sum S with only coins of 3 and 5. (S > 7)
S = int(input("The sum for you to pay is: "))
# S = x * 3 + 5 * y
if S % 3 == 0:
    x = S // 3
    y = 0
    print("It can be paid with only coins of 3.")
elif S % 3 == 1:
    x = S // 3 - 3
    y = 2
    print(f"We can pay with coins of 3 and 5. We will need {x} of 3 and {y} of 5.")
 # S = 3 * unknown_no + 1
 # unknown_no = S / 3 => S = 3 * S / 3 + 1
 # remember the equation form :  S = x * 3 + 5 * y
 # x and y have to be integers so we can't do 1 / 5 = y. Let's try with the smallest multiple of five, 10.
 # that means we'll substract a 9 from 3 * S / 3 = 3 * x
 # S = 3 * S / 3 - 9 + 5 * 2
 # S = 3 * S / 3 - 3 * 3 + 5 * 2
 # S = 3 * (S / 3 - 3) + 5 * 2
 # => x = S / 3 - 3   and    y = 2 
elif S % 3 == 2:
    x = S // 3 - 3
    y = 2
    print(f"We can pay the sum with {x} of 3 and {y} of 5.")




