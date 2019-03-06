arr = []   #创建列表
print(type(arr))

t = (1,2,3,4,2,2,2)   #创建元组
print(type(t))
print(t)

#两种遍历方式
for x in t:
    print(x,end = ' ')
    print()

for i in range(len(t)):
    print(t[i],end = ' ')
    print()

#计算给定元素的下标
i = t.index(3)
print(i)

#统计给定元素在元组中出现的次数
count = t.count(2)
print(count)

#如果创建的元组中只有一个元素，必须在元素后添加','
t = (1,)
print(type(t))