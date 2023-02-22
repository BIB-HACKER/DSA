# [1, 2, 2, 3, 5, 6]
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

ln=m+n-1
while(m>0):
    nums1.pop(-1)
    m-=1
i=0
while(i<n):
    nums1.append(nums2[i])
    i+=1
# [1, 2, 3, 2, 5, 6]
i=1
while(ln>i):
    j=0
    while(j<ln-i):
        if nums1[j]>nums1[j+1]:
            nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
        j+=1  
    i+=1

print(nums1)














# list1=[]
# for i in range(m):
#     list1.append(nums1[i])
# for j in range(n):
#     list1.append(nums2[j])
# list1.sort()
# print(list1)