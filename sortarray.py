from array import *

num = array('i',[5,9,4,6,7])
print('Before sort:  ',end='')
print(num)

for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print('After sort:  ',end='')
print(num)