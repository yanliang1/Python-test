#打开文件
f = open("a.txt","wb")
print(type(f))

#写到文件中去时，有格式错误，那就需要编码
res = f.write("hello python".encode())
print("res =",res)

#关闭文件
f.close()
