from functools import reduce

def mult(x,y):
    return x*y

nums = range(1,5)
print('1# list of nums = ',list(nums))

product = reduce(mult,nums)
print('2# Total product:',product)

product = reduce(lambda x,y:x*y,nums)
print('3# = (((1*2)*3)*4) = ',product)

product = reduce(lambda x,y:x*y,nums,2)
print('4# = ((((2*1)*2)*3)*4) = ',product)

product = reduce(mult,nums,2)
print('5# Total product:',product)

total = reduce(lambda x,y:x+y,nums)
print('1# Total = (((1+2)+3)+4) = ', total)

total = reduce(lambda x,y:x+y,nums,2)
print('2# Total = ((((2+1)+2)+3)+4) = ', total)

total = sum(nums)
print('3# total sum = ', total)
total = sum(nums,2)
print('4# total sum = ', total)
