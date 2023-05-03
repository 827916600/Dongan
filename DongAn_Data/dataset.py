import numpy as np

path= '/Users/wupeng/PycharmProjects/Fault_monitoring/Data/DongAn_Data/anormal.txt'

# 打开txt文件
with open(path, 'r') as file:
    # 读取文件内容
    lines = file.readlines()
    # 创建空列表
    my_list = []
    # 遍历每行文本，并添加到列表中
    for line in lines:
        # 转换为数字
        num = float(line.strip())
        my_list.append(num)
    # 打印列表
    print(len(my_list))


