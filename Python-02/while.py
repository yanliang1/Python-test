#while循环示例
#求1-100的和

# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num += 1
    
# print(sum)

# #从键盘输入用户名和密码，如果不正确，提示用户，继续输入，知道正确为止
# username = input("请输入用户名：")
# password = input("请输入密码：")

# while username != "root" or password != "123456":
#     print("用户名或密码不正确！请重新输入！")
#     username = input("请输入用户名：")
#     password = input("请输入密码：")

# print("登录成功！")

print("------------------猜数字---------------------")
import random
num = random.randint(1,101)
guess = int(input("请输入1-100内的随机数字："))
count = 1
while guess != num:
    if guess > num:
        print("猜错了，必随机数要大!")
        count += 1
    elif guess < num:
        print("猜错了，比随机数要小!")
        count += 1
    else:
        pass
    guess = int(input("请输入1-100内的随机数字："))
print("恭喜您，猜对了，总共用了",count,"次","这个数就是：",num)