import math


def JumpOnTheClouds(c):
    thunder_index = []
    result = 0
    for i in range(0,len(c)):
        if c[i] == 1:
            thunder_index.append(i)
    for i in range(0, len(thunder_index)-1):
        next = thunder_index[i]+1
        prev = thunder_index[i+1]-1
        count = math.ceil((prev - next)/2)
        result += count
    result += len(thunder_index)
    result = result + math.ceil((thunder_index[0]-1-0)/2) + math.ceil((len(c)-1-thunder_index[-1]-1)/2)
    return result


c = [0,0,0,1,0,1,0,0,1,0,0,0,]
print(test(c))



