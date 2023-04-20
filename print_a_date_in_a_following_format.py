# Print a date in the following format:
# Day_name Day_number Month_name Year

from datetime import datetime
given_date = datetime(2023, 4, 19)
print("Given date is:")
print(given_date.strftime("%A %d %B %Y"))

# strptime - parse a string into a datetime obj given a correspondant format
# strftime - convert obj to a string according to a given format
# %A - weekday full name
# %d - day of month as a zero-padded decimal number
# %B - month full name
# %Y - year without century
