# Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

# Note: Return -1 if you can't reach the end of the array.

# Example 1:

# Input:
# N = 11 
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to the last. 
# Example 2:

# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}
# Output: 2 
# Explanation: 
# First we jump from the 1st to 2nd element 
# and then jump to the last element.

class Solution:
	def minJumps(self, arr, n):
	    if n == 1:
            return 0
        if arr[0] == 0:
             return -1
        step,maxi,jump=0,0,0
            
        for i in range(n-1):
            maxi=max(maxi,arr[i]+i)  # 
            if i==step:
                jump+=1 
                step=maxi
                if step>=n-1:
                    return jump
        return -1
    
if __name__=="__main__":
     N = 11 
     arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]        
     ob=Solution()
     print(ob.minJumps(arr,N))



