# case1= {4,-4,6,-6,10,-11,12}
# case2 = {-4,4,-6,6,-10,11,-12}

def kadane(arr,n):
    currsum=0
    maxsum=0
    for i in range(n):
        currsum+=arr[i]
        if currsum<0:
            currsum=0
        maxsum=max(maxsum,currsum)
        
    return maxsum

arr=[4,-4,6,-6,10,-11,12] # (-11) Non-Contributing element
n=len(arr)

wrapsum=0
nonwrapsum=0

nonwrapsum=kadane(arr,n)  # 12 MAX

totalsum=0
for i in range(n):
    totalsum+=arr[i]  # 11 SUM
    arr[i]=-arr[i] #[-4, 4, -6, 6, -10, 11, -12]

wrapsum=totalsum + kadane(arr,n)# <-  11 MAX (kadane[-4, 4, -6, 6, -10, 11, -12])
# wrapsum = 11 -(-11) = 22

print(max(nonwrapsum,wrapsum))