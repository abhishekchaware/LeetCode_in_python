'''
Input: nums = [1,3,5,6], target = 5
Output: 2
'''
nums = [1,3,5,6]
target = 7
def insert_ele(nums,target):
    l=0
    r = len(nums)-1
    
    while l <r:
        mid = (l+r)//2
        if target==nums[mid]:
            return mid
        elif nums[mid] < target:
            l =mid+1
        else:
            r =mid -1
    return l
print(insert_ele(nums,target))