#class的基本使用

class Person:
    def __init__(self,name,age):   #this
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def study(self):
        print("I'm studying python now!")

class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y
    def move(self,x,y):
        self.__x = x
        self.__y = y


if __name__ == "__main__":
    admin = Person("WuZui",21)   #实例化一个对象
    print(type(admin))
    print(admin.get_name(),admin.get_age())

    root = Person("yl",22)
    print(root.get_name(),root.get_age())  #通过方法访问对象属性

    root.study()

    p1 = Point(100,200)
    p2 = Point(0,0)
    p2.set_x(300)
    p2.set_y(400)
    print(p1.get_x(),p2.get_x())
    p1.move(p2.get_x(),p2.get_y())
    print(p1.get_x())
