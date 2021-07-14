'''
******  we can use another code for below program   ******
****** Easy code ****

from array import *
vals = array('i',[19,5,6,1,88])

newarr = array(vals.typecode , (a*a for a in vals))

for i in newarr:
    print(i)

'''

from array import *
vals = array('i',[9,5,8,3,4,5])

# this syntax is use to copy array to another array

newarr = array(vals.typecode , [a*a for a in vals])

for i in range(len(newarr)):
    print(newarr[i])