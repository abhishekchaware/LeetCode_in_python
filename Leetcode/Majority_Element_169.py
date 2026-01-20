'''
Docstring for Leetcode.Majority_Element_169
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(nums:list[int]) -> int:
    d ={}
    lenn = len(nums)
    for  i in range(lenn):
        if nums[i] not in d:
            d[nums[i]] =1
        else:
            d[nums[i]] +=1
    srt = sorted(d.items(),key= lambda x: -x[1])
    return srt[0][0]

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))