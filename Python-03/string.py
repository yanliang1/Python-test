# find()           查找（*）
# join()           加入
# replace()        替换（*）
# lower()          小写
# split()          切分（*）
# strip()          去空
# format()         格式（*）
# count()          统计
# index()          索引
# endswith()       是否以某字符串结束
# startswith()     是否以某字符串开始

string = "hello python"
print(string)
index = string.find('python')  #查找 找到返回其下标，没找到返回-1
print("index =",index)

print("----------------------------------")

path = ["home","gec","tool"]  #连接 /home/gec/tool
string = "/".join(path)
print(string)
print(type(string))

print("----------------------------------")

string = "hello"
string2 = '#'.join(string)   #连接 
print(string2)

print("----------------------------------")

string3 = string2.replace("#",",")   #替换
print(string2)
print(string3)

print("----------------------------------")

string = "hello python"
print(string.upper())  #大写：HELLO PYTHON
print(string.lower())  #小写：hello python
print(string.title())  #标题：Hello Ptthon

print("----------------------------------")

path = "/usr/local/arm/bin"
# path = path.replace("/"," ")
# print(path)
res = path.split('/')   #切分,默认以空白字符为切分点，也可自己指定切分字符和字符串
print(type(res))   #切分后的得到的是一个列表
print(res)

print("----------------------------------")

string = "  hello  world  "
res = string.strip()   #去除字符串两边的空格，返回一个新的字符串
print(string)
print(res)

print("----------------------------------")

a = 10
b = 20
print("{} + {} = {}".format(a,b,a + b))   #格式字符串   # 10 + 20 = 30

print("----------------------------------")

string = "/home/csgec/abc.mp3"
print(string.endswith(".mp3"))   #是不是以.mp3结尾
print(string.endswith(".mp4"))