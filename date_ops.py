from datetime import datetime

def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    delta = abs(d2 - d1)
    return delta.days
