import os


i = 1
while i < 20:
# 改次数
    old_path = 'E:\\44Programmar\Class_22_homework\\2-Advanced'
# 改路径
    dir_name = f'郑炳辉-201804032-第{i}次作业-A'
    new_path = os.path.join(old_path, dir_name)
# 把旧的路径和新创建的文件夹路径合在一起形成一个新的路径
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print(f"Path is created {i}")
    i += 1

print('OK! GOOD LUCK! Master!')



