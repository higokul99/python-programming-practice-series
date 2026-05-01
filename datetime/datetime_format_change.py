from datetime import datetime

input_date = "2026-04-23"

# converting input_date string to datetime object
datetime_obj = datetime.strptime(input_date, "%Y-%m-%d")

# converting the input_date to desired output format
formatted_date = datetime_obj.strftime("%d-%b-%Y")

print(formatted_date)