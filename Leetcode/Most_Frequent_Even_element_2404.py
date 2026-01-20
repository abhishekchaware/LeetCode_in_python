'''
Docstring for Leetcode.Most_Frequent_Even_element_2404

Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.
Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
'''

def mostFrequentEven(nums: list[int]) -> int:
    d ={}
    lenn = len(nums)
    for i in range(lenn):
        if nums[i]%2==0:
            if nums[i] not in d:
                d[nums[i]] =1
            else:
                d[nums[i]] +=1
    if not d:
        return -1
    srt = sorted(d.items(),key=lambda x: (-x[1],x[0]))
    return srt[0][0]

nums = [4,4,4,9,2,4]
print(mostFrequentEven(nums))