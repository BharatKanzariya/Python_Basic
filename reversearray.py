'''
***** CODE FOR FIXED SIZE ARRAY ******

from array import *

a1 = array('i',[4,8,9,5,6])
print(a1)

a2 = array('i',[])

for i in range(4,-1,-1):
    x = a1[i]
    a2.append(x)

print(a2)
'''

# ********* CODE FOR VARIABLE AYYAY *******

from array import *

n = int(input('Enter length of array: '))
a1 = array('i',[])

for i in range(0,n):
    x = int(input('Enter array element: '))
    a1.append(x)

print(a1)

rev = array('i',[])

for j in range(len(a1)-1,-1,-1):
    y = a1[j]
    rev.append(y)

print(rev)