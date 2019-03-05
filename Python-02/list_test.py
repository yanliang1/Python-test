#用随机生成的10个数创建一个列表，求其最大值与最小值
import random
arr = []
i = 0
for i in range(10):
    num = random.randint(1,100)
    arr.append(num)
print(arr)

#利用内置的函数求列表的最大值与最小值
print("最大值为：",max(arr))
print("最小值为：",min(arr))

#自定义实现求列表的最大值与最小值
j = 0
max_value = arr[j]
for j in range(0,len(arr)):
    if arr[j] > max_value:
        max_value = arr[j]
    else:
        pass
print("最大值为：",max_value)

x = 0
min_value = arr[x]
for x in range(0,len(arr)):
    if arr[x] < min_value:
        min_value = arr[x]
    else:
        pass
print("最小值为：",min_value)

#系统内置函数的排序
arr.sort()  #默认从小到大
print(arr)

#给一个整数列表排序，利用冒泡排序算法(自己写的)
y = 0
z = 0
temp = 0   #中间变量
for y in range(len(arr) - 1):    #外层循环控制比较轮数
    for z in range(len(arr) - 1 - y):  #内层循环控制比较次数
        if arr[z] > arr[z + 1]:
            temp = arr[z]
            arr[z] = arr[z + 1]
            arr[z + 1] = temp 
print(arr)