import datetime
# from datetime import datetime

# 写一个进行时间计算，比如加减
now = datetime.datetime.now()
print(now)

new_now = now + datetime.timedelta(hours=7)
print(new_now)

new_now2 = now + datetime.timedelta(days=11)
print(new_now2)

new_now3 = now + datetime.timedelta(days=3, hours=10)
print(new_now3)


# 写一个时间转字符串,字符串转时间
# 字符串转时间
day = datetime.datetime.strptime('2018-6-1 13:13:13', '%Y-%m-%d %H:%M:%S')
print(type(day), day)

# 时间转字符串
now = datetime.datetime.now()
new_day = now.strftime('%Y-%m-%d %H:%M:%S')
print(type(new_day), new_day)


# 写一个时区变更
utc_dt = datetime.datetime.utcnow()
print(utc_dt)
bj_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
print(bj_dt)

