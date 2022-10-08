from datetime import date, datetime, timedelta, time

# delta = timedelta(
# 	days=50,
# 	seconds=27,
# 	microseconds=10,
# 	milliseconds=29000,
# 	minutes=5,
# 	hours=8,
# 	weeks=2
# )

# print(delta.days)
 
## // ## ## // ## ## // ## ## // ## ## // ## ## // ## 

# x = timedelta(days = 10, seconds = 40)
# y = timedelta(days = 20, hours = 7, minutes = 20)

# z = y-x
# print(z)
# print(z.total_seconds())
 
## // ## ## // ## ## // ## ## // ## ## // ## ## // ## 

# data = date(2022, 6, 8)
# x = date.fromisoformat(str(data))
# y = x.strftime("%d:%m:%Y")
# print(y)

## // ## ## // ## ## // ## ## // ## ## // ## ## // ## 

# x = datetime.today()
# y = timedelta(days = 10, hours = 20, minutes = 10)
# z = x+y

# semanas = ['Seg','Ter','Qua','Qui','Sex','Sab','Dom']
# zz = z.weekday()
# print(semanas[zz])

## // ## ## // ## ## // ## ## // ## ## // ## ## // ## 
x = time(hour=2, minute=50, second=0, microsecond=0)
print(x)