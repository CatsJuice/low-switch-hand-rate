import os
import pandas as pd

def bubble_sort(arr):
    res = arr[:]
    n = len(res)
    for i in range(n-1):
        for j in range(n-1-i):
            if res[j]['rate'] > res[j+1]['rate']:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

def print_percent(n):
    print("[", end='')
    print('#' * n, end='')
    print(' '*(100-n), end='')
    print(']', n, '%')

# 遍历所有股票
file_path_prefix = 'F:\\files\\sharesDatas\\kline\\'
fileList = os.listdir(file_path_prefix)

all_rate = []

all_sum = len(fileList)
flag_num = 0
pre = 0
cur = 0

for file_name in fileList:
    code = file_name[0:6]
    data = pd.read_csv(file_path_prefix + file_name, encoding="gbk")
    arr = data.head(20)
    datas = arr.values
    if len(datas) < 20:
        continue
    all = 0
    for item in datas:
        all += float(item[10])
    averageRate = all / 20
    dic = {
        'code': code,
        'rate': averageRate
    }
    all_rate.append(dic)

    flag_num += 1
    persent = flag_num * 100 // all_sum
    cur = persent
    if cur != pre:
        print_percent(persent)
        pre = cur


print('')
print(all_rate)
sorted_arr = bubble_sort(all_rate)
print(sorted_arr)

all = 10
count = 0

for i in range(10):
    print(i, ':', sorted_arr[len(sorted_arr)-1-i])