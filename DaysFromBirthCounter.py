from datetime import datetime, timedelta

BD = input("What si your Brithdate? (yyyy/mm/dd)")
def time_since(BD):
    date_obj = datetime.strptime(BD, '%Y/%m/%d')
    delta = datetime.now() - date_obj
    return delta

time_elapsed = time_since(BD)
print(f"From {BD} passed: {time_elapsed.days} days.")
print(f"From {BD} passed: {time_elapsed.days/30} months.")
print(f"From {BD} passed: {time_elapsed.days/365} years.")