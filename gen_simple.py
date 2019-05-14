def abc_generator():
    yield 'a'
    yield 'b'
    yield 'c'

for char in abc_generator():
    print(char)

print('##-----------------------##')

def num_generator(num=1):
    while num:
        yield num
        num +=1

for num in num_generator():
    if num !=5:
        print(num)
    if num == 10:
        print('Yayaya done!!!')
        break

print('##-----------------------##')

def doubles(stop):
    return (10*n for n in range(stop))

double_gen = doubles(2)
print('double _gen type = ', type(double_gen))
print('double _gen 1st = ', next(double_gen))
print('double _gen 2nd = ', next(double_gen))
print('double _gen 3rd = ', double_gen.__next__())
print('double _gen 4th = ', double_gen.__next__())






