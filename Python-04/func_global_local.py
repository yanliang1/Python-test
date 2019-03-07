#函数中变量的作用域

string = "hello"  #全局变量

def func():
    num = 100  #局部变量只在这个函数中使用
    # string = "python"  #这里相当于重新定义了string
    global string  #加上这条语句，则为声明string为全局变量
    string = "你好"
    print(num,string)
    # print(string)  #在函数内部也可使用全局变量

func()
# print(num)  #报错，num没有定义

print(string)