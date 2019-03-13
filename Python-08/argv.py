#命令行参数的典型示例
import sys

#查看命令行参数的个数
print(len(sys.argv))

#查看命令行参数的内容
print(sys.argv)

if len(sys.argv) != 2:
    print("参数个数不对，使用方式：xxx.py<单词>")
    sys.exit(1)

print("参数正确，程序继续执行！")

input("press any key to continue...")