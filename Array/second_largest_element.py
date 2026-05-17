num = [12,7,9,6,60,34]

def second_largest(num):
    n = len(num)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
    
    # print("the second largest number is :- ",num[-2])
    return num[-2]

print(second_largest(num))   
