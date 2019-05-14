def odd(val):
    return val % 2
nums = range(10)
print('nums in list= ',list(nums))

odds = filter(odd, nums)
print('odds filter object = ',odds)

odds = list(filter(odd, nums))
print('odds filter list = ',odds)

odds = list(filter(lambda val:val%2, nums))
print('another odds filter list = ',odds)


odds = [num for num in nums if num % 2]
print("aaanother odds method",odds)

##########
def ncar(val):
    return val.endswith('n')
vehicles = ['sedan','coupe','hatchback','wagon']
print('list of vehicles = ', vehicles)

ncars = list(filter(ncar,vehicles))
print('List of ncats = ', ncars)

ncars = list(filter(lambda val:val.startswith('h'),vehicles))
print('List of ncars start with h = ', ncars)

ncars = [car for car in vehicles if car.endswith('e')]
print('List of ncars end with e = ', ncars)
