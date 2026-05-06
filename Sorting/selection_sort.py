num = [5,7,8,4,1,6,9,2]

def selection_sort(num):
    n = len(num)
    for i in range(0,n):
        mini_index=i
        for j in range(i+1,n):
            if num[j]<num[mini_index]:
                mini_index = j
        num[i],num[mini_index]=num[mini_index],num[i]

selection_sort(num)
print(num)