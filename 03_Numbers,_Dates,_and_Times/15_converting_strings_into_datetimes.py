from datetime import datetime

date_text = '2013-03-01'

a = datetime.strptime(date_text, '%Y-%m-%d')
b = datetime.now()
print(b - a)

print(datetime.strftime(b, '%A %B %d, %Y'))
