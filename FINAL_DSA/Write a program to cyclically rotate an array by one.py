def rotate( arr, n):
    # l=[]
    # l.insert(0,arr[-1])
    # for i in range(0,n-1):
    #     l.append(arr[i])
    # return l
    
    a=arr[-1]
    # arr.pop(n-1)
    del arr[-1]
    arr.insert(0,a)

if __name__=="__main__":
    N = 5
    A =[1, 2, 3, 4, 5]
    rotate(A,N)
    print(*A)
