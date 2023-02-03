import time
import datetime

# today = datetime.date.today()
today = datetime.datetime.today()
# today1 = datetime.datetime.now()

# print(today)
# print(today1)

year = today.year
month = today.month
day = today.day

# --- 1

# print(year, month, day)

# year_born = 23
# print(year - 23)

# print(today - datetime.timedelta(days=365.2425 * 23))

# --- 2

birth_date = datetime.datetime.strptime("2003-04-03", "%Y-%m-%d")
# print((today - birth_date).days / 365.2425)

# temp = 0
# if birth_date.month > today.month:
#     temp = 1
# elif birth_date.month == today.month:
#     if birth_date.day > today.day:
#         temp = 1

# tuple comparing
temp = ((today.month, today.day) < (birth_date.month, birth_date.day))

delta_year = today.year - birth_date.year - temp
print(delta_year)
