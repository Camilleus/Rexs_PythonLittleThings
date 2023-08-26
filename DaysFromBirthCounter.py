from datetime import datetime, timedelta

BD = input("What si your Brithdate? (yyyy/mm/dd)")
date_obj = datetime.strptime(BD, '%Y/%m/%d')

"""
#ITS FIRST VERSION OF IT    
def time_since(BD):
    delta = datetime.now() - date_obj
    return delta

time_elapsed = time_since(BD)
print(f"From {BD} passed: {time_elapsed.days} days.")
print(f"From {BD} passed: {time_elapsed.days/30} months.")
print(f"From {BD} passed: {time_elapsed.days/365} years.")
"""
def time_since(date_obj):
    now = datetime.now()
    delta = now - date_obj

    years = (now.year - date_obj.year)
    if now.month < date_obj.month or (now.month == date_obj.month and now.day < date_obj.day):
        years -= 1

    months = now.month - date_obj.month
    days = delta.days - years * 365

    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return years, months, days, hours, minutes, seconds

years, months, days, hours, minutes, seconds = time_since(date_obj)
print(
    f"From {date_obj} passed: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")


