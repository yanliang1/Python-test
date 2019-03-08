PYTHON-DAY01:
1.文件共享方式：
	1.ftp://172.16.53.186
	2.飞秋
2.环境安装
	1.anaconda3
	2.vscode
	3.vnc

3.测试是否安装成功
	开始菜单->
	Anaconda3(32-bit)
	->Anaconda Prompt
	输入ipython,按回车
-------------------------
4.编程语言
	解释型:python shell JS 	解释器
	编译型:C C++ Java C#...	编译器

	python ipython

	关于执行效率(速度)：
		编译型语言执行速度比解释型语言的执行速度要快。

		不要在意执行速度。
		关注开发效率！

5.第一个python程序
	print("hello world")  	#输出
	input()					#输入

	执行方式1：
		打开anaconda prompt
		切换到代码所在目录
		例：
		切换到D盘：
			D:
		进入到代码目录：
			cd D:\2019_03_python\01
		用解释器解释你的python脚本
			python hello.py
	执行方式2：
		设置环境变量
		C:\ProgramData\Anaconda3\
		C:\ProgramData\Anaconda3\Scripts
		C:\ProgramData\Anaconda3\Library\bin
		把以上三个路径添加到环境变量中。
		环境变量：右键[计算机]->属性->
		高级系统设置->环境变量->系统变量->Path
		注：Path中的路径是以分号分隔的


6.基本要素-数据类型
	任何编程语言都必须能描述(表示)数据项
	int 	整数（没有任何限制）
	float	小数
	str 	字符串
	bool 	布尔(True False)
	.....
	python实现的是动态类型机制，一个变量可以接受任意类型的值，随着值不同，类型也会不同

	类型转换:
		数据类型名(表达式/值)
	例：
		int('123') 	=> 指把字符串“123”转换成数字123


7.基本要素-变量
	C:  		类型名  变量名;
	python:		变量名 = 值
	命名规则 ：
		1.只能由数字，字母及下划线，且不能以数字开头
			如:	name  age 
				1name(错误)
		2.不能用语言的关键字来命名
			输入以下指令，查看关键字有哪些： 
				help("keywords")
		3.见名知其义，不建议用拼音
		4.python中区分大小写  
			name  Name   =>这是两个变量名


8.基本要素-运算符
	算术运算符	+ - *  /  //(整除)  %  **(幂运算)
	关系运算符	> >= < <=  == !=  
					if(a>=0 and a<10)--> if( 0<=a<10 )
	逻辑运算符
				and 	#与
				or		#或
				not		#非	
	...


9.分支语句 if
	格式：
		if(布尔表达式):
			语句块
		elif(布尔表达式):
			语句块
		...
		else:
			语句块

	注：python中没有大括号来包含语句块，用冒号配合缩进来替代大括号
		建议所有的缩进用Tab键(4个空格)

	练习：
		从键盘输入一个年份，判断这一年是不是闰年

	

第二天：
回顾：
	环境安装：一定要在安装时把anaconda注册到系统的环境变量
	解释型
	编译型
		ipython

	print()
	input()
	#
	对齐

	int 
	float
	str   ""  ''   '''hello python'''
	bool True False
	type()

	int("123")
	类型名(表达式)

	if

------------------
1.编程要素-循环结构(for while)
	for循环格式：
		for 循环变量名 in 序列:
			语句块

	for循环用循环变量依次获取序列的每个元素，对每个元素执行一次循环体(代码块)

序列：最基本的数据结构，是数据元素(如数字，字符等)的集合
		其中每个元素都有一个编号(位置/下标/索引)
		序列的第一个元素的索引为0，第二个元素的索引为1，依次类推。


	range(start,end)
		生成从start到end的一个序列，取值范围  [start,end)
		例：
			range(1,10)  =>  [1,10)  1 2 3 4 5 6 7 8 9



练习：
	用for循环计算所有的水仙花数
	实现九九乘法表
		print("hello",end=' ') #print不换行
		print("python")


	鸡兔同笼：
		鸡有两只脚，兔有四只脚(没有例外)，笼子中只总共100只脚，
		问：有多少只鸡？多少只兔子？


2.while循环
	格式：
		while 布尔表达式:
			语句块

	说明：只要条件(布尔表达式)为真(True)，循环体重复执行，如果条件为假(False)，循环终止。


	练习 ：猜数字
			随机数：random.randint(start,stop)	
					在这个范围[start,stop]中随机生成一个整数

					例：random.randint(1,100)

3.两个关键字
	break
	continue



4.序列
	列表(list)	元组	(tuple)	 字符串(str)

	列表：	动态数组  
	元组：	不可修改的列表
	字符串： 字符序列   

列表：
	创建
		array = []
	操作：
		添加
		修改
		删除
		遍历

	练习：
		用随机生成10个数字创建一个列表，求其中的最大值和最小值。
		max()
		min()


		给一个整数列表排序，用冒泡排序法
			两两比较，如果前面的值比后面的值大，就交换他们

	->	5 4 3 2 1
		4 5 3 2 1
		4 3 5 2 1
		4 3 2 5 1
		4 3 2 1 5

		3 4 2 1 5
		3 2 4 1 5
		3 2 1 4 5

		2 3 1 4 5
		2 1 3 4 5

	->	1 2 3 4 5


第三天的Python内容：
回顾：
	流程控制
		if 布尔表达式:
			代码块
		elif 布尔表达式:
			代码块
		...
		else:
			pass

		for 循环变量 in 序列:
			代码块

		while 布尔表达式：
			代码块

		序列
			列表		任意类型 任意个数
				创建：[]
				添加：append()
				修改：array[0] = 1
				删除：pop() remove() del
				遍历：
					for x in 列表:
					for i in range(0,len(列表)):

				len()
				min()
				max()
				sort()
				clear()
				index()


			元组		不可修改的列表
				创建：()
				遍历：与列表同
				索引：index()
				统计：count()
			
			字符串：str
				find()		查找
				join()		加入
				replace()	替换
				lower()		小写
				split()		切分
				strip()		去空
				format()	格式
				count()		统计
				index()		索引
				endswith()	是否以某字符串结束
				startswith()是否以某字符串开始

		序列的通用操作：
			相加		相乘		切片		长度   成员资格(in)


		练习：
			用户输入年月日 如  2019 3 1
			输出结果如下：
				Mar 1st 2019
				Mar 2nd 2019
				Mar 3rd 2019
				Mar 4th 2019

			months = ["Jan","Feb","Mar","APr","May","Jun","July","Aug","Sept","Oct","Nov","Dec"]

			ends = ["st","nd","rd"]+["th"]*17+["st","nd","rd"]+["th"]*7+["st"]


		列表生成式
			列表名 = [表达式 for 变量 in 序列 if 布尔表达式]
			例：
				a = [i**2 for i in range(5) if i%2 != 0]
				说明： 循环变量 i 从序列(0-4)中获取每个元素，然后判断是不是奇数，如果是则计算变量i的平方，最终把得到的结果做为列表的一个元素。




		映射
			字典	dict
				字典中存储的 不是单个的值，而是由键(key)和值(value)组成的一对元素(项 item)
				键：不可变类型 如数字 字符串 元组
				值：任意类型
				键值对表示方式
					键:值

			创建：{}
			添加：字典名[key] = 值
			修改：字典名[key] = 值   #如果字典中键不存在，则添加，存在则修改
			删除：clear() pop()
			查询：items() keys() values() get()
			
			拷贝：copy()    

			练习：
				如果用get去获取指定的值，发现键不存在，会返回什么结果？None

				"""
				{
					"Type":"ASM",
					"DeviceID":"45",
					"Policy":"this is my policy",
					"A":
						{
						"B":45,
						"C":46
						}
				}
				"""

-----------------------------------------
函数：
	函数是一个命名了的代码块，通过函数名调用执行相应的代码块。
	
	内置函数
		len() max() min()  ...
	自定义函数
		格式：
			def 函数名(参数列表):
				函数体

	函数的参数：
		位置参数(*)
		默认参数(*)
		可变参数
			思考：
			传递一个列表给求平均值的函数，如果列表中还包含字符串，这个时候该怎么处理？？
			[1,2,3,4,'hello',5]
		关键字参数
		命名关键字参数(*)
			print(a,b,end=' ')

第四天的Python内容：
回顾：
	类型
		int
		float
		str
		bool

		列表 list []
			append()
			remove() pop() del
			下标 
			index() 
			len()
			max()
			min()
			sort()
			reverse()
		元组 tuple ()
			index()
			count()

		字符串 str
			find()
			replace()
			split()
			join()
			format()
		+  * 切片 长度  索引

		字典 dict {}
			key value
			[key] = value
			get()
			keys()
			values()
			items()


		函数
			def 函数名(参数列表):
				函数体
				return None

			函数名()

			位置参数
			默认参数
			可变参数  	*参数名
			关键字参数	**参数名
			命名关键字参数 	,*,

			作用域		
		
			递归
				在函数内部，调用函数自身	

				阶乘
					n!
					1! = 1			1
					2! = 2*1		2*1!
					3! = 3*2*1		3*2!
					4! = 4*3*2*1	4*3!

				幂运算
					power(x,n)

					2**0
						1
					2**1
						2*1
					2**2
						2*2
					2**3
						2*2*2
					2**4
						2*2*2*2

---------------------------------------
类(class)和对象		object
	对象：一切皆对象
	类：类型	自定义类型
		类 类型的变量，就是对象
		类 描述的对象的 属性和行为

	定义类：
		class 类名:
			pass


	实例化对象：	
		对象名 = 类名()

	练习：
		定义一个日期类型,提供年月日，计算这是一年中的第几天，要考虑闰年
		
		class Date:
			pass


		date = Date(2019,3,7)
		days = date.which_day()
		print(days)



------------------------
opencv   开源计算机视觉库
在线安装：
	打开命令行，执行如下指令
		pip install opencv-python

离线包安装：
	打开命令行，执行如下指令
		pip install 安装包名

测试：
	进入python命令行
	import cv2


-------------------------------
1.图像的基本操作
	打开图片
		obj = cv2.imread(图片名)
	显示到窗体中
		cv2.imshow("img",obj)
	等待操作
		cv2.waitKey(0)
	销毁窗体
		cv2.destroyAllWindows()


2.基本概念
	像素:图像的基本组成单位
	分辨率	宽x高	1024x768(一行有1024个像素点,总共768行)
	宽 	单位是像素点
	高
	位深:一个像素点由多个位(bit)组成
		一般的图像的位深是 24位
	分量/通道: 一个像素点由几个字节组成,如24位的图像,那就是3通道的

	彩图:	一个像素点由	RGB 三个分量组成
	灰度图:	灰度值		0-255
	黑白:	二值图  要么是0  要么是255

	读取图像的像素:
		图片对象[y:x]		#[行:列]
	修改图像的像素值:
		图片对象[行:列] = [蓝,绿,红]
		图片对象[起始行:结束行,起始列:结束列] = [蓝,绿,红]

	保存图像:
		cv2.imwrite(图片名,图片对象)
