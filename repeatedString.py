def repeatedString(s, n):
    if len(s) == 1:
        count = n
        return count

    string = []
    j = 0
    for i in range(0,n):
        string.append(s[j])
        j += 1
        if j == len(s):
            j = 0
    count = string.count(s[0])
    return count



s = 'aba'
n=10
print(repeatedString(s,n))