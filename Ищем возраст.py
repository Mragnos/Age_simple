import datetime
from calendar import monthrange


def days_in_month(year, month):
    return monthrange(year, month)[1]


def is_valid_date(year, month, day):

    if datetime.MINYEAR <= year <= datetime.MAXYEAR \
            and 1 <= month <= 12 and 1 <= day <= days_in_month(year, month):
        return True
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):

    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        diff = date2 - date1
        if date2 > date1:
            return diff.days
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):
    today = datetime.date.today()
    if is_valid_date(year, month, day):
        return days_between(year, month, day, today.year, today.month, today.day)
    else:
        return 0


your_year = int(input('В каком году вы родились?: '))
your_month = int(input('В каком месяце?: '))
your_date = int(input('Какого числа?: '))
print(age_in_days(your_year, your_month, your_date))
