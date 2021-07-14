# 0 1 1 2 3 5 8 13 21 34 55 89
# 1 1 2 3 5 8 13 21 34 55 89
# both are fibonacci series for first take i=0,j=1 and for second take i=1,j=1

def fibo(n):
    a = 0
    b = 1
    if n == 0:
        pass
    elif n== 1:
        print(a)
    else:
        if n < 0:
            print('Please Enter Positive Value')
        else:
            print(a)
            print(b)

            for i in range(2,n):
                c = a + b
                print(c)
                a = b
                b = c

fibo(-8)
