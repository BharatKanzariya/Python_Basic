from functools import reduce

nums = [5,2,9,4,3,7,2,1,4]

evens = list(filter(lambda n : n%2==0,nums))
print(evens)

squares = list(map(lambda n : n*n,evens))
print(squares)

sum = reduce(lambda a,b : a+b ,squares)
print(sum)