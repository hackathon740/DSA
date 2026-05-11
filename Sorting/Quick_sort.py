num = [4,1,7,6,2,8,9,3]

def partition (num,low,high):
    pivot = num[low]
    i,j=low,high
    while i<j:
        while num[i]<=pivot and i<=high-1:
            i+=1
        while num[j]>pivot and j>=low+1:
            j-=1
        
        if i<j:
            num[i],num[j]=num[j],num[i]
    num[low],num[j]=num[j],num[low]
    return j        

def quick_sort(num,low,high):
    if low<high:
        p_index = partition(num , low , high)
        quick_sort(num,low,p_index-1)
        quick_sort(num,p_index+1,high)

quick_sort(num, 0, len(num)-1)
print(num)