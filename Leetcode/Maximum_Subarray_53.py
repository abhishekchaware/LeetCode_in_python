'''
Docstring for Leetcode.Maximum_Subarray_53
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

'''

def maxSubArray(nums: list[int]) -> int:
    maxsumm = nums[0]
    summ =0
    lenn = len(nums)
    for i in range(lenn):
        summ +=nums[i]
        maxsumm = max(summ,maxsumm)
        if summ <0:
            summ =0
    return maxsumm

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))