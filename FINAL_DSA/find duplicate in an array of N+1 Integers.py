# Given an numsay of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the numsay nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

class Solution:
    def findDuplicate(self, nums ):
        nums.sort()
        for i in range(1,len(nums)):
            # if nums.count(nums[i])>1:
            #    return nums[i]
            # if nums[i-1] in nums[i:]:
            #     return nums[i-1] 
            if nums[i-1]==nums[i]:
                return nums[i]
            

                         
           
if __name__=="__main__":
    nums=[3,1,3,4,2]
    on=Solution()
    print(on.findDuplicate(nums))