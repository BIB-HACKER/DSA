class pair:
    def __init__(self):
        self.min=0
        self.max=0

def getminmax(arr,n):
    minmax=pair()

     # If there is only one element then return it as min and max both
    if n==1:
       minmax.max=arr[0]
       minmax.min=arr[0]

    # If there are more than one elements, then initialize min and max
    if arr[0]>arr[1]:
        minmax.max=arr[0]
        minmax.min=arr[1]
    else:
        minmax.max=arr[1]
        minmax.min=arr[0]

    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max=arr[i]
        elif arr[i]<minmax.min:
            minmax.min=arr[i]

    return minmax

#Driver code
if __name__ == "__main__":
    arr=[1000,11,445,1,330,3000]
    arr_size=6
    minmax=getminmax(arr,arr_size)
    print("Minimum element is ",minmax.min)
    print("Maximum element is ",minmax.max)

#- - - - - - - - - - - - - - - - - - - - - - - -

# def getminmax(arr,s,e):
#     arr_max=arr[s]
#     arr_min=arr[s]

#     # If there is only one element
#     if s==e:
#         arr_max=arr[e]
#         arr_min=arr[s]
#         return (arr_max, arr_min)
    
#     # If there is only two element
#     elif e==s+1:
#         if arr[s]>arr[e]:
#             arr_max=arr[s]
#             arr_min=arr[e]
#         else:
#             arr_max=arr[e]
#             arr_min=arr[s]
#         return (arr_max, arr_min)
    
#     # If there are more than 2 elements
#     else :
#         mid =int((s+e)/2)  
#         arr_max1, arr_min1 = getminmax(arr,s,mid) # 0,1,2 -> 0,1 
#   #  1  (1000)    (11)
#   #  2     
#         arr_max2, arr_min2 = getminmax(arr, mid+1,e) # 2,2 -> 3,4,5 ->  
#   #  1   (445)     (455) 

#     return (max(arr_max1,arr_max2)), (min(arr_min1,arr_min2))


# arr=[1000,11,445,1,330,3000]
# start=0
# end=len(arr)-1
# arr_max, arr_min = getminmax(arr,start,end)
# print('Minimum element is ', arr_min)
# print('nMaximum element is ', arr_max)