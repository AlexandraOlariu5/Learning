date_string = "18/04/2023"
import datetime
date_object = datetime.datetime.strptime("18/04/2023", "%d/%m/%Y").date()
print(date_object)
