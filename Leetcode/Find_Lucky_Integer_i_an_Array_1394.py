"""
Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
    
"""
arr = [1,2,2,3,3,3]
Output: 3

def findLucky(nums) -> int:
        d = {}
        lenn = len(nums)
        for i in range(lenn):
            if nums[i] not in d :
                d[nums[i]] = 1
            else:
                d[nums[i]] +=1
        srt = dict(sorted(d.items(),key = lambda x : x[0],reverse = True))
        for k , v in srt.items():
            if k==v:
                return k
        return -1
print(findLucky(nums=arr))