s = "programming"

freq = {}

# Count frequency
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Sort characters by frequency
sorted_chars = sorted(freq, key=freq.get, reverse=True)

# Print characters
for ch in sorted_chars:
    print(ch, freq[ch])

result = ""
for ch in sorted_chars:
    result += ch*freq[ch]
print(result)
