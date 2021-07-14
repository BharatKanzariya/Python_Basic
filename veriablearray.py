from array import *

val = array('i',[])

n = int(input('Entaer value of n: '))

for i in range(n):
    x = int(input('Enter value: '))
    val.append(x)

print(val)

s = int(input('Entaer value for serch: '))

for i in range(n):
    if val[i] == s:
        print('Index number for serch eliment is= ',i)

# below index method is print index of the element if there are two element same
# in search,index method print only first index of searching element.

print('*** Below index number is print by index method. ***')
print('First index no of searching element is: ',end='')
print(val.index(s))