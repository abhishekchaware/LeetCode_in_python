"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
nums = [-1,2,1,-4]
target = 1

def threeSumClosest(nums: list[int], target: int) -> int:
    lenn = len(nums)
    nums.sort()
    close=float("inf")
    curr = 0
    for i in range(lenn-2):
        l = i+1
        r = lenn-1
        while l < r:
            curr = nums[i]+nums[l]+nums[r]
            if abs(curr - target) < abs(close-target):
                close = curr
            if curr < target:
                l +=1
            elif curr > target:
                r -=1
            else:
                return target
    return close

print(threeSumClosest(nums,target=target))