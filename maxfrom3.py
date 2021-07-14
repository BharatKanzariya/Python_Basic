x = int(input('enter 1 no:'))
y = int(input('enter 2 no:'))
z = int(input('enter 3 no:'))
if x > y :
    if x > z :
        print('maximum is',x)
    else:
        print('maximum is',z)
else:
    if y > z :
        print('maximum is',y)
    else:
        print('maximum is',z)
