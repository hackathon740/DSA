num = [5,7,8,4,1,6,9,2]

def insertation(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and num[j]>key :
            num[j+1]=num[j]
            j-=1
        num[j+1]=key

print(insertation(num))
print(num)