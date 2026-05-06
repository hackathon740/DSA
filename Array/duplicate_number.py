num = [1,3,4,2,2,4,2]

dict={}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
max_val = max(dict, key=dict.get)
print(max_val)