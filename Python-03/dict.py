#键值对（字典）->映射

d = {}    #创建
print(type(d))
print(len(d))

#添加
#d[key] = value
d["red"] = 0xff0000
d["green"] = 0x00ff00
d["blue"] = 0x0000ff
print(len(d))
print(d)

#修改
d["red"] = 123456
print(len(d))
print(d)

#移除
d.pop("red")
print(d)

#获取指定的值
value = d.get("green")
print("value =",value)

print("-"*30)

#获取所有的项
print(d.items())
#获取所有的键
print(d.keys())
#获取所有的值
print(d.values())

print("---------------------------")

for k,v in d.items():
    print(type(k),type(v))
    print(k,v)