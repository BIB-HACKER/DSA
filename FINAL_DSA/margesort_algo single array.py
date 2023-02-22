def margeb(a,low,mid,high,b):
    i,j,k=low,mid,low
    while(i<mid and j<high):
        if a[i]>a[j]:
            b.append(a[i])
            i+=1
            k+=1
        else:
            b.append(a[j])
            j+=1
            k+=1
    
    while(i>mid):
        b.append(a[i])  
        k+=1
        i+=1

    while(j>high):
        b.append(a[j])  
        k+=1
        j+=1
    
    
    for i in range(low,high):
        arr[i]=b[i]

arr=[2 ,4 ,1, 3, 5]
b=[]
low=0
mid=len(arr)//2
high=len(arr)

margeb(arr,low,mid,high,b)
print(arr)