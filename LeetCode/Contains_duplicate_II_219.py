'''
Input: nums = [1,2,3,1], k = 3
Output: true
'''
nums = [1,0,1,1]
k = 1

def chek(nums,k):
    d={}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            if i - d[nums[i]] <=k:
                return True
            d[nums[i]] =i 
    return False

print(chek(nums,k))