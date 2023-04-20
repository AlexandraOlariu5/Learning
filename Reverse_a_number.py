# Reverse a number

x = int(input("Choose a number, preferable with at least 2 digits "))
reverse = 0
i = 0
while x > 0:
    reminder = x % 10
    reverse = (reverse * 10) + reminder
    x = x // 10

print("Reverse: ", reverse)
  