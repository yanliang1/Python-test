#字典使用示例
d = {"root":"123456","abc":"123","admin":"456"}

username = input("请您输入用户名：")
password = input("请您输入密码：")

if username in d.keys():
    if d.get(username) == password:
        print("登录成功！")
    else:
        print("密码错误！")
else:
    print("用户名不存在！")

#如果用get去获得指定的值，发现键不存在，会返回None
result = d.get("wz")
print(result)