from deadline import Deadline
from datetime import date

correct_date = Deadline(2003,9,24)

print(f"{correct_date.task_day}/{correct_date.task_month}/{correct_date.task_year}")
