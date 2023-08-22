from datetime import datetime, timedelta
particular_date = datetime(2002, 8, 20)
new_date = datetime.today() - particular_date
print (new_date.days)