f1 = open('info','r')

f2 = open('info2.txt','a')

for data in f1:
    f2.write(data)