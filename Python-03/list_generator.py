# a = []
# for i in range(1,11):
#     a.append(i)
# print(a) 

#列表生成式的几种表示方法
a = [i for i in range(1,11)]
print(a)

a = [i * 2 for i in range(1,11) if i % 2 == 0]
print(a)

import random
a = [random.randint(1,99) for i in range(10)]
print(a)

a = ["{}*{}={}".format(i,j,i*j) for i in range(1,10) for j in range(1,i + 1)]
print(a)