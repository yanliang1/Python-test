#序列的通用操作
#相加 相乘 切片 长度 成员资格

#字符串列表的加法
str1 = "hello"
str2 = "python"
str3 = str1 + " " + str2
print("str3 = {}".format(str3))

a = [1,2,3]
b = ["hello","world"]
c = a + b
print(c)
print(a)
print(b)

a = (1,2,3)
b = ("hello","world")
c = a + b
print(type(c))
print(c)

print("----------------------------")

# 乘法操作
s1 = "hello"
print("s1.len = {}".format(len(s1)))
s2 = s1 * 3
print("s2 = {}".format(s2))
print("s2.len = {}".format(len(s2)))

d = a * 3
print(type(d))
print(d)

print("-" * 30)

#成员资格
result = "hello" in s2
print("result = {}".format(result))

a = [1,2,3,4]
result = 10 in a
print("result = {}".format(result))

print("---------------------------")

#切片 切取序列中的部分内容
a = [1,2,3,4,5,6,7,8]
b = a[0:3]    #序列[开始位置:结束位置]  取值范围 -> [开始位置:结束位置)
print(type(b))
print(b)

string = "hello python"
b = string[1:]   #结束位置可省略，表示直到序列结束，开始位置也可省略，表示从零开始
print(type(b))
print(b)

c = a[:]   #起始位置和结束位置都可省略，表示为复制
print(type(c))
print(c)

c = a[-5:-2]   #索引可以为负值
print(c)

print("-"*30)

a = [1,2,3,4,5]
b = a
print(b)

c = a[:]
print(c)
a[0] = 100

print(a)
print(b)
print(c)

print(a is b)   #身份运算符
print(a is c)