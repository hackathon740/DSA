s = [1,2,3,4,5]
def rev(s,left,right):
    if left>=right:
        return
    s[left],s[right]=s[right],s[left]
    rev(s,left+1,right-1)

rev(s,0,len(s)-1)
print(s)   