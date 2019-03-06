#列表嵌套

a = [1,2,3,4,5]
b = [6,7,8,9,0]
c = [a,b]
print(len(c))
print(len(c[0]))
print(len(c[1]))
print(c)
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j],end = '')

print()