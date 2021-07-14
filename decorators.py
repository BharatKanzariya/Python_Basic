def div(a,b):
    print(a/b)

def smart(func):

    def change(c,d):
        if c<d:
            c,d = d,c
            return func(c,d)
    return change

ndiv = smart(div)

ndiv(2,4)