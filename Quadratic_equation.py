# Second grade ecuation
import math
print("choose a coefficient 'a': ")
a = float(input())
print("choose a coefficient 'b': ")
b = float(input())
print("choose a coefficient 'c': ")
c = float(input())
print()

# ecuation = a * x ** 2 + b * x + c == 0
# ecuation = (x - x1) * (x + x2)
delta = b ** 2 - 4 * a * c
x1 = 0
x2 = 0
if delta == 0:
    x1 = x2 = -b / 2 * a
    print(x1)

elif delta > 0:
    x1 = (-b + math.sqrt(delta))/ 2 * a 
    x2 = (-b - math.sqrt(delta))/ 2 * a
    print(x1)
    print(x2)
elif delta < 0:
    print("No solution")





