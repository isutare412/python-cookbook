from datetime import datetime
import pytz

utc_now = datetime.now(pytz.utc)
seoul_now = utc_now.astimezone(pytz.timezone('Asia/Seoul'))
la_now = seoul_now.astimezone(pytz.timezone('America/Los_Angeles'))
print(utc_now)
print(seoul_now)
print(la_now)
