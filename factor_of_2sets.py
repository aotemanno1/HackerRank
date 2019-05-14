"""there is a number, temp, which max(a)<temp<min(b), how many number like this
    exist?"""
a = [2, 4]
b = [16, 32, 96]

# a=[2,6]
# b=[6,12]

# a=[2,6]
# b=[4,12]

a.sort()
b.sort()
count = 0
count2 = 0
result = 0
temp = [0]
temp2 = []
temp3 = []
if a[-1] == b[0]:
    for i in range(len(a)):
        if b[0] % a[i] == 0:
            temp[0] = b[0]
        else:
            count = 0
            print(count)
    for j in range(len(b)):
        if b[j] % temp[0] != 0:
            count = 0
            print(count)
        else:
            count = 1
    print(count)

elif a[-1] > b[0]:
    count = 0
    print(count)

elif a[-1] < b[0]:
    isCopy = True
    print(temp2)
    index = 0
    for i in range(a[-1], b[0] + 1):
        for j in range(len(a)):
            if i % a[j] != 0:
                isCopy = False
                break
            else:
                isCopy = True
                index = i
        if isCopy:
            temp2.append(index)
    '''temp2 can divide list a'''
    print('list a = ', a)
    print('temp2 = ', temp2)
    print('list b = ', b)

    isCopy = True
    # for i in range(len(b)):
    #     print('---- i=%i ----' %i)
    #     for j in range(len(temp2)):
    for j in range(len(temp2)):
        print('---- i=%i ----' %i)
        for i in range(len(b)):
            '''find how many in temp2 can be divided by b'''
            if b[i] % temp2[j] == 0:
                count2 += 1
                if count2 == len(b):
                    result += 1
            else:
                count2 = 0

        # temp3.append(count2)
        count2 = 0

    print(temp3)
    print(result)
