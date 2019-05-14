pi = 3.1415926

def numbers(stop=10):
    num_list = []
    for n in range(1,stop+1):
        print('adding %s to the num_list' % n)
        num_list.append(n)
    return num_list

def area_circle(radius):
    area = pi * radius ** 2
    print('Circle area with radius %s is: %s' % (radius,area))
    return area

num_list = numbers()
area_list = [area_circle(n) for n in num_list]
print('The list of area is: ', area_list)

print('###-------------------###')
print('\nCreate values with lazy evaluation')

def numbers_gen(stop=10):
    n = 1
    while n<stop+1:
        print('yielding n as :%s' %n)
        yield n
        n+=1

def area_circle_gen(radius):
    area = pi*radius **2
    print('circle area with raidus %s is: %s' %(radius,area))
    yield area

area_list_gen = (area_circle_gen(n) for n in numbers_gen())
print('area_list_gen type = ',type(area_list_gen))
print('areas = ')
for area in area_list_gen:
    print(next(area))

