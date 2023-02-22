# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.

# Example 2:

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        con_sum=0
        max_sum=arr[0]
        for i in range(N):
            con_sum+=arr[i]
            max_sum=max(max_sum,con_sum)
            if con_sum<0:
                con_sum=0
        return max_sum   

if __name__=="__main__":
    N=5
    arr=[1,2,3,-2,5]
    # arr=[-1,-2,-3,-4]
    ob=Solution()
    print(ob.maxSubArraySum(arr,N))
