num = int(input("enter the given number :- "))
result = []
for i in range(1,num+1):
    if i%2==0:
        result.append(i)
    else:
        pass
print("the factors are",result)