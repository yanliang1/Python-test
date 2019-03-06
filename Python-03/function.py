#函数使用示例

#先定义再调用
def foo():
    print("hello python")
    a = [i for i in range(10)]
    print(a)

def main():
    foo()
    print("-"*10)
    print(__name__)

def is_leap(year):  #位置参数
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("{}是闰年！".format(year))
        return True
    else:
        print("{}是平年！".format(year))
        return False

def sum(num1,num2):  #位置参数
    return num1 + num2

def power(num,n = 2):  #默认值参数
    res = 1
    for i in range(n):
        res = res * num
    return res

#求n个数的平均值
def average(*array):  #可变参数
    print(type(array))
    sum = 0
    for num in array:
        sum += num
    return sum/len(array)

#关键字参数
def get_info(name,age,**option):
    print("name:",name)
    print("age:",age)
    print(type(option))
    print("option:",option)

def show_list(array,sep = ' '):
    for i in range(len(array)):
        print(array[i],end = '')
        print(sep,end = '')
    print()

#命名关键字参数
def connect(ip,db,*,user,pwd):
    print("ip:",ip)
    print("user:",user)
    print("pwd",pwd)
    print("db",db)

def return_values():
    x = 100
    y = 200
    z = 300
    return x,y,z

if __name__ == '__main__':
    main()
    foo()
    ok = is_leap(2100)
    print("ok =",ok)
    s = sum(10,20)
    print(s)
    print(power(4))
    print(power(3,3))
    a = [1,2,3,4]
    avg = average(1,2,3,4,5)
    print("avg =",avg)
    print(average(*a))
    get_info("zhangfei",20)
    get_info("guanyu",22,addr = "ChangSha", 武器 = "青龙偃月刀")
    print("------------------------------")
    show_list(a,sep = '#')

    connect("192.168.1.110","test.db",pwd = "123",user = "root")

    x,y,z = return_values()
    print("x =",x,"y =",y,z)