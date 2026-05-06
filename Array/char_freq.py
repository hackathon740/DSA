s = "azysseruioop"
q = ["a","s","i","o"]

freq = {}
for i in s:
    freq[i] = freq.get(i,0) + 1

result = {}
for i in q:
    result[i] = freq.get(i,0)

print(result)    