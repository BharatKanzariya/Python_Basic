num = int(input('Enter number for calculate factoriyal: '))

sum = 1

for i in range(1,num+1):
    sum = sum * i
    i += 1

print('Factoriyal of',num,' is= ',sum)
