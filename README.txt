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

	

	


