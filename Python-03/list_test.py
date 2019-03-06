#案例：用户输入例如 2019 3 6 这种日期，要求输出为：Mar 6th 2019 这种格式

year = int(input("请您输入当前年份："))
month = int(input("请您输入当前月份："))
day = int(input("请您输入当前日期："))

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep",
"Oct","Nov","Dec"]

ends = ["st","nd","rd"] + ["th"] * 17 + ["st","nd","rd"] + ["th"] * 7 + ["st"]

if months[month - 1] in months and ends[day - 1] in ends:
    print(months[month - 1],"{}{}".format(day,ends[day - 1]),year)