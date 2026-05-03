num = [5,6,7,7,1,9,1,1,1,5,1,7]
dict = {}
for i in range(0,len(num)):
    if num[i] in dict:
        dict[num[i]]+=1
    else:
        dict[num[i]]=1
print(dict)