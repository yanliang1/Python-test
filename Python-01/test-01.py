num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
operator = input("请输入运算符：")
if(operator == "+"):
    num3 = num1 + num2
    print("结果为：",num3)
elif(operator == "-"):
    num3 = num1 - num2
    print("结果为：",num3)
elif(operator == "*"):
    num3 = num1 * num2
    print("结果为：",num3)
elif(operator == "/"):
    num3 = num1 / num2
    print("结果为：",num3)
else:
    print("您输入有误，请重新输入！")

