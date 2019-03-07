#提示用户输入一个日期，要求计算是那一年的第几天，考虑闰年

class Data:
    def __init__(self):
        self.__year = int(input("请您输入年份："))
        self.__month = int(input("请您输入月份："))
        self.__day = int(input("请您输入日期："))

day = Data()
