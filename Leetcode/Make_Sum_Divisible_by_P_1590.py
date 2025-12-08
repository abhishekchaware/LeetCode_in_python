"""
Input: nums = [6,3,5,2], p = 9
Output: 2
"""
nums = [6,3,5,2]

p = 7
# l = []
# lenn = len(nums)
# i = 0
# while i < lenn:
#     res = sum(nums[i:i+2])
#     if p == res:
#         len1 = len(nums[i:i+2])
#         for i in range(len1):
#             l.append(nums[i])
#             nums.pop(i)
#     i +=1
# print(l,nums)
def minSubarray(nums , p):
    val = 0
    summ =sum(nums)
    res = summ %p
    lenn = len(nums)
    if res ==0:
        return val 
    else:
        if res in nums : 
            val +=1
            lenn -=1
        else:
            j=0
            while j < lenn:
                if res == sum(nums[j:j+2]):
                    len1= len(nums[j:j+2])
                    val +=len1
                    for i in range(len1):
                        nums.pop(i)
                        lenn -=1
                else :
                    return -1
                j +=1
                    
                    
print(minSubarray(nums=nums,p=p))