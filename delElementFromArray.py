'''

***** FOR FIXED SIZE ARRAY *****

from array import *

a1 = array('i',[2,9,6,8,3])
print(a1)

for i in range(0,len(a1)):
    if i == 2:
        a1[2]=a1[3]
        a1[3]=a1[4]

a1.pop()
print(a1)
'''

# ****** FOR VARIABLE ARRAY *******


from array import *

n = int(input('Enter length of array: '))
a1 = array('i',[])

for i in range(0,n):
    x = int(input('Enter array element: '))
    a1.append(x)

print(a1)

e = int(input('Enter index number for delete item: '))

if e<n:
    for i in range(0,len(a1)):
        if i == e:
            p = i
            while p<n-1:
                a1[p]=a1[p+1]
                p += 1

    a1.pop()
    print(a1)
else:
    print('Wrong input')