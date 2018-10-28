import os


path = 'C:\\Users\Alex\Desktop\Memorandum\\test.md'
#Dont't forget to modify the path.
with open(path, 'r') as f:
    lines = f.readlines()
with open(path, 'w') as f:
    for i in lines:
        f.write(i.replace('C:\\Users\Alex\AppData\Local\Temp', 'E:\\88pic\pic'))
        #Don't forget to modify the characters.

