'''
You are given an integer array nums.
A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.


Example 1:
Input: nums = [1,2,1,1,3]
Output: 6

Explanation:
The minimum distance is achieved by the good tuple (0, 2, 3).
(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.
'''
nums = [1,2,1,1,3]
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        d ={}
        flag =False
        minval = float("inf")
        for i , num in enumerate(nums):
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]
            if len(d[num]) >= 3:
                flag =True
                r = d[num][-1]
                l = d[num][-3]
                minval = min(minval , 2 * (r-l))
        if not flag:
            return -1
        return minval
s = Solution()
print(s.minimumDistance(nums))
