"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
    """

def majorityElement(nums) -> list[int]:
    lenn = len(nums)
    d ={}
    for i in range(lenn):
        if nums[i] not in d:
            d[nums[i]]=1
        else:
            d[nums[i]] +=1
    if not d:
        return
    srt = sorted(d.items(),key = lambda x:(-x[1],x[0]))
    n = lenn//3
    return [x[0] for x in srt if x[1] > n]

nums = [3,2,3] 
print(majorityElement(nums))