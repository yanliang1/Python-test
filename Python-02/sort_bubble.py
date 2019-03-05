#交换两个变量的值
a = 10
b = 20 
print(a,b)
# tmp = a
# a = b
# b = tmp
a,b = b,a
print(a,b)

#老师写的
# array = [5,4,3,2,1]
array = [1,2,3,4,5]
print("begin:",array)
for i in range(len(array) - 1):
    is_sorted = True
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j],array[j + 1] = array[j + 1],array[j]
            is_sorted = False
    if is_sorted == True:
        break
    else:
        print("->",array)
print("after:",array)