# multi dimentional array

from numpy import *

arr1 = array([
                [4,8,9,5,9,6],
                [6,3,4,3,9,7]
                ])

print(arr1)
print('Total no of dimention: ',arr1.ndim)
print('Number of rows and coloms: ',arr1.shape)
print()
print()

arr2 = arr1.flatten()
print('flotten convert multidimentional array into 1d array:',arr2)
print()
print()

arr3 = arr2.reshape(6,2)
print(arr3)
print()
print()

arr4 = arr2.reshape(3,2,2)
print(arr4)
print()
print()

m = matrix(arr1)
print(m)