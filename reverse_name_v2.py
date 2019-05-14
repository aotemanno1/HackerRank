name = input()
full_name = list(name)
pos = full_name.index(' ')#position of ' '
length = len(full_name)
first = str('')
last = str('')
for i in range(pos):
    first = first+full_name[i]

for j in range(pos,length):
    last = last+full_name[j]
print(first[::-1] +' '+ last[::-1])
