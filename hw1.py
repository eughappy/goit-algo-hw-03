import datetime as dt
from datetime import timedelta
from datetime import datetime as dtdt
def get_days_from_today(date):
    time_now = dtdt.today()
    try:
        time_then = dtdt.strptime(date, '%Y-%m-%d')
    except:
        date = str(input("Введіть дату: "))
        get_days_from_today(date)
    days_gone = (time_now - time_then)
    return(abs(days_gone.days))

date = str(input("Введіть дату: "))
print(get_days_from_today(date))