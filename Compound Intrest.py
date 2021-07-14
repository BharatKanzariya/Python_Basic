n = 40000
s = 40000

y = int(input('Enter Year:'))

for i in range(y):
    vyaj = (12*s)/100
    s = s + vyaj
    print("total:",n," After vyaj:",s)
    s = s + n
