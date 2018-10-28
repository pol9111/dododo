import re

# 1开头， 接3/4/5/7/8， 再接9个数字
s = re.findall(r'^1[34578][0-9]{9}\b', '18950076568 1')
print(s)

s = re.findall(r'^1[3-578]\d{9}$', '13139500765')
print(s)

# 英文字母开头， 接4-15位英文数字下划线
s = re.findall(r'^[a-zA-Z][a-zA-Z0-9_]{4,15}$', 'pol911_')
print(s)

s = re.findall(r'^[a-zA-Z][a-zA-Z0-9_]{4,15}$', 'pol411_789012345')
print(s)







