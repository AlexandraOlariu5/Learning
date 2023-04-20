from datetime import datetime
given_date = datetime(2023, 4, 19)
print(given_date.today().weekday())
print(given_date.strftime("%A"))
