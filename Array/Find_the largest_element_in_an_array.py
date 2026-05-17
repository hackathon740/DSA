num = [1,5,7,2,9,-2]

def largest(num):
    larg = num[0]

    n = len(num)
    for i in range(0,n):
        larg = max(larg,num[i])
    return larg
print(largest(num))