# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

# Example 2:

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 of element (-1)

def kadane(arr,n):
    con=0
    maxi=arr[0]
    for i in range(n):
        con+=arr[i]
        maxi=max(con,maxi)
        if con<0:
            con=0
    return maxi

if __name__=="__main__":
    n=5
    arr=[1,2,3,-2,5]
    print(kadane(arr,n))