import datetime as dt
from datetime import datetime as dtdt
from datetime import timedelta

def get_upcoming_birthdays(users):
    #today = dtdt.today().date()
    today = dtdt(year = 2024, month = 1, day = 22).date()
    result = []
    for user in users:
        birthday = dtdt.strptime(user["birthday"], '%Y.%m.%d').date()
        birthday_this_year = dtdt(year = today.year, month = birthday.month, day = birthday.day).date()
        week_day = birthday_this_year.isoweekday()
        quant_days = (birthday_this_year - today).days
        if 1 <= quant_days <=7:
            if week_day == 7:
                result.append({"name":user["name"],"congratulation_date":(birthday_this_year + timedelta(days=1)).strftime('%Y.%m.%d')})
            elif week_day == 6:
                print(birthday_this_year + timedelta(days=2))
                result.append({"name":user["name"],"congratulation_date":(birthday_this_year + timedelta(days=2)).strftime('%Y.%m.%d')})
            else:
                result.append({"name":user["name"],"congratulation_date":birthday_this_year.strftime('%Y.%m.%d')})

    return result




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)