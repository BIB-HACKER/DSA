# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output:-12  -13  -5  -7  -3  -6  11  6  5

l=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
le=[]

for i in range(len(l)):
    if l[i]<0:
        le.append(l[i])

for j in range(len(l)):
    if l[j]>=0:
        le.append(l[j])

print(*le)