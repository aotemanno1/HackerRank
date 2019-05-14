print('For loop:')
seq = 'abcde'
for char in seq:
    print(char,end = ' ')

print('\nwhile loop:')
index = 0
while index < len(seq):
    print(seq[index], end=' ')
    index += 1

seq_upper = [c.upper() for c in seq]
tup_pairs = zip(seq,seq_upper)
print('\nis tup_paris iterable?',hasattr(tup_pairs,'__iter__'))
print('For loop:')
for pair in tup_pairs:
    print(pair,end=' ')
    break


print('\nIs tup_paris an iterator?', hasattr(tup_pairs,'__next__'))
print('Iteration #2', tup_pairs.__next__())

print('\nIs tup_paris an iterable?', hasattr(seq,'__iter__'))
print('\nIs tup_paris an iterator?', hasattr(seq,'__next__'))

it = iter(seq)
print('\nIs it an iterable?', hasattr(it,'__iter__'))
print('\nIs it an iterator?', hasattr(it,'__next__'))

##print('#1', it.__next__())
##print('#2', it.__next__())
##print('#3', it.__next__())
##print('#4', it.__next__())
##print('#5', it.__next__())
##print('#6', it.__next__())

#test
print("START TESTING")
my_list = [4,7,0,3]
my_iter = iter(my_list)
print(my_iter.__next__())
print(my_iter.__next__())
