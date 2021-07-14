a = 5

def fun():
    a = 9
    print('inside the function',end=' ')
    x = globals()['a']
    print(x)
    print(id(x))

fun()

print('outside the function',a)
print(id(a))