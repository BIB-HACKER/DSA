#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        # i=1
        # while i<n-1:
        #     j=0
        #     while j<n-i:
        #         if arr[j]>arr[j+1]:
        #             arr[j],arr[j+1] = arr[j+1], arr[j]
        #         j+=1
        #     i+=1
        #------
        i=1
        if i==1:
            j=0
            while j<n-i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                j+=1
            i+=1
        if i==2:
            j=0
            while j<n-i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                j+=1
            i+=1
        if i==3:
            j=0
            while j<n-i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                j+=1
            i+=1
        if i==4:
            j=0
            while j<n-i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                j+=1
            i+=1
        if i==5:
            j=0
            while j<n-i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                j+=1
            i+=1
        #--------
        # a = 0
        # b = 0
        # c = 0
        # for i in range(n):
        #     if arr[i] == 0:
        #         a += 1
                
        #     elif arr[i] == 1:
        #         b += 1
                
        #     elif arr[i] == 2:
        #         c += 1
                
                
        # j=0
        
        # while(a>0):
        #     arr[j] = 0
        #     j += 1
        #     a -= 1
            
        # while(b>0):
        #     arr[j] = 1
        #     j += 1
        #     b -= 1
            
        # while(c>0):
        #     arr[j] = 2
        #     j += 1
        #     c -= 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    n=5
    arr=[0,2,1,2,0]
    ob=Solution()
    ob.sort012(arr,n)
    print(*arr)    
    

# } Driver Code Ends