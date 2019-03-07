#递归函数

# def test_rec():
#     print("这是递归函数的测试")
#     test_rec()

# test_rec()
# print("程序到此结束")

#阶乘(递归算法)
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))

#阶乘（非递归）
def factorial_norec(num):
    result = 1
    if num == 1:
        return 1
    else:
        for i in range(2,num + 1):
            result *= i
        return result

print(factorial_norec(5))

#幂运算（递归）
def power_plus(num,n):
    if n == 0:
        return 1
    return num * power_plus(num,n - 1)

print(power_plus(2,3))