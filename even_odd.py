# Even/ Odd test
print("Please enter an integer: ")
x = input()
list_of_evens = []
list_of_odds = []
i = 0
while True:
    for i in x:
        if int(i) % 2 == 0:
            list_of_evens.append(i)
        else:
            list_of_odds.append(i)
print("Evens: ", list_of_evens)
print("Odds: ", list_of_odds)






