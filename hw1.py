import datetime as dt
from datetime import timedelta
from datetime import datetime as dtdt
def get_days_from_today(date):
    time_now = dtdt.now()
    time_then = dtdt.strptime(date, '%Y-%m-%d')
    days_gone = (time_now - time_then)
    print(abs(days_gone.days))

date = str(input("Введіть дату: "))
get_days_from_today(date)