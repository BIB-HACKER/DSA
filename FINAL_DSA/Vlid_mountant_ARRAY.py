# Given an array of integers arr, print true only if it is a valid mountain array else print false. recall that arr is a valid mountain array if and only if :
# arr.length>=3
# there exists some i with 0<i<arr.length-1 susch that :
# > arr[0]<arr[1]<...........<arr[i-1]<arr[i]
# > arr[i]>arr[i+1]>............>arr[arr.length-1]
# arr=[1,3,5,6,5,3,1,0]#################################
# arr=[1,3,5,6,7,8,9]

n=int(input("->"))
arr=[]
for i in range(n):
    arr.append(int(input("enter value =")))
j=0
while j+1<n and arr[j]<arr[j+1]:
    j+=1

if j==0 or j==n-1:
    print("False")
else:
    while j+1<n and arr[j]>arr[j+1]:
       j+=1

    if j==n-1:
           print("True") 
    else:
          print("False")
###############################################
arr=[1,3,5,6,5,3,1,0]

max1=0
for i in arr:
    if max1<i:
        max1=i
flag=False
for i in range(0,len(arr)):
    if arr[i]<max1:
        flag=True
        continue
    else:
        flag=False
        break
for j in range(len(arr)-1,-1,-1):
    if arr[j]<max1:
        flag=True
        continue
    else:
        flag=False
        break
print(flag)




