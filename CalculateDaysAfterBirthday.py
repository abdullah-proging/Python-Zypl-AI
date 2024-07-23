from datetime import date

dateBirthday = date(2010, 6, 8)
dateToday = date.today()

print((dateToday - dateBirthday).days)