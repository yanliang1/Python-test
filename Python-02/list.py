#list基本操作

#创建列表
arr = []
print(type(arr))

#查看大小
size = len(arr)
print(size)

#添加元素
arr.append(1)
arr.append("hello")
arr.append(3.14)
arr.append([1,2,3])
print(len(arr))

#列表的遍历
for i in range(0,len(arr)):
    print(arr[i],end = ' ')
print()

print(arr)

#列表的修改
for i in range(0,len(arr)):
    arr[i] = i**2
print()

print(arr)

#列表的删除
del arr[0]   #从列表中删除指定位置的值
print(arr)

arr.remove(9)  #从列表中删除指定的值
print(arr)