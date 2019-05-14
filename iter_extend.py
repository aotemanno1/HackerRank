try:
    a,b,c = 1,2,3,4
except ValueError as err:
    print('Handled ValueError:', err)
    print('\n')

a,b,*c = 1,2,3,4
print('a=',a)
print('b=',b)
print('c=',c)
print('\n')

a,b,*c='hello'
print('a=',a)
print('b=',b)
print('c=',c)
print('\n')

a,*b,c='hel333333333lo'
print('a=',a)
print('b=',b)
print('c=',c)
print('\n')

first, *last = {1:'a',2:'b',3:'c',4:'d'}
print('first = ',first)
print('last = ',last)
print('\n')
