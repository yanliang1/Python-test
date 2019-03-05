#这是if语句的示例代码
#从键盘输入一个数，判断是否大于零

# num = input("请输入一个数字：")
# num = int(num)#把输入的字符串转换成整数

# if(num > 10):
#     print(num,"大于10！")
# elif(num == 10):
#     print(num,"等于10！")
# else:
#     print(num,"小于10！")

print("---------------------------")
#判断一个年份是不是闰年
#闰年分为：普通闰年：即为能被4整除不能被100整除的年份
#         世纪闰年：即为能被400整除的年份
year = int(input("请输入一个年份："))

if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("不是闰年")