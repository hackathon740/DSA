num = [5,7,8,4,1,6,9,2]

def bubble_sort(num):
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

bubble_sort(num)
print(num)
