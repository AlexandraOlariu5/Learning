x = [1, 23, 67, 3238, 744, 90, 75]
evens = []
odds = []

for i in x:
    if i % 2 == 0:
        evens.append(i) 
    else:
         odds.append(i)
print("Evens: ", evens)
print() 
print("Odds: ", odds)

