import datetime

a = datetime.timedelta(days=2, hours=6)
b = datetime.timedelta(hours=4.5)
c = a + b

print(c.days)
print(c.seconds / (60 * 60))
print(c.total_seconds() / (60 * 60))
print()

a = datetime.datetime(2013, 3, 1)
print(a + datetime.timedelta(days=10))
print()

b = datetime.datetime(2013, 3, 31)
print(b - a)
print()

now = datetime.datetime.today()
print(now)
print(now + datetime.timedelta(minutes=-10))
