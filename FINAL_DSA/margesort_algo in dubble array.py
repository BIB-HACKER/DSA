def margesort(a,b,m,n,sort):
    i,j,k=0,0,0
    while(i<m and j<n):
        if a[i]<b[j]:
            sort.append(a[i])
            i+=1
            k+=1
        else:
            sort.append(b[j])
            j+=1
            k+=1
    
    while(i<m):
        sort.append(a[i])   # COPY ALL REMAINING ELEMENT FROM a TO sort)
        k+=1
        i+=1

    while(j<n):
        sort.append(b[j])  # COPY ALL REMAINING ELEMENT FROM b TO sort)
        k+=1
        j+=1

    return k

arr=[2, 4, 1, 3, 5]
u=len(arr)//2
a=[]
b=[]
sort=[]
for i in range(u+1):
    a.append(arr[i])
for j in range(u+1,len(arr)):
    b.append(arr[j])
a.sort()
b.sort()
m=len(a)
n=len(b)

print(margesort(a,b,m,n,sort))


    