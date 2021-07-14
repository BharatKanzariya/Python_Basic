'''
****** my own code for prime or not prime number ******
num = int(input('Enter any number:'))
if num > 1 :
    r = int(num / 2)
    count = 2
    i = 2
    while i <= r:
        count += 1
        if num % i == 0:
            print('Not prime')
            break
        else:
            i += 1
    if count == i:
        print('Prime')
else:
    print('1 is constant number.')
'''

# this is online code
num = int(input('Enter any number:'))
if num > 1 :
    for i in range(2,num):
        if(num % i == 0):
            print('Not prime')
            break
# when break is executed then else condition is skip
# And if break is not executed then else is executed
    else:
        print('prime')
else:
    print('1 is constant number.')