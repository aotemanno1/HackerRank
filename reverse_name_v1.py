name = input()
full_name = list(name)
pos = full_name.index(' ')#position of ' '
length = len(full_name)
first = str('')
last = str('')
for i in range(pos-1,-1,-1):
    first = first+full_name[i]
##print(first)

	
for j in range(length-1,pos,-1):
    last = last + full_name[j]
##print(last)
print('first method: '+first+' '+last)


