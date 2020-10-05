"""
datetime
"""
import datetime

# 日時
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H:%M:%S:%f'))

# 日付
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 時刻
t = datetime.time(hour=1, minute=10, second=30, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H:%M:%S:%f'))

# 差分
print(now)
#d = datetime.timedelta(hours=1)
#d = datetime.timedelta(days=1)
d = datetime.timedelta(weeks=1)
print(now + d)

# time sleepやepoctimeを取得
import time

print('#### waiting 1 sec... ####')
time.sleep(1)
print('#### finished ####')
print(time.time())
