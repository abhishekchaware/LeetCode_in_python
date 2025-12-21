nums = [2,4,1,1,6,5]

def x(nums):
    lenn = len(nums)
    i=1
    summ = 0
    while i < lenn -1:
        l = i-1
        while (l >=0) and (nums[i]==nums[l]):
            l -=1
        r = i+1
        while (r < lenn)and(nums[i]==nums[r]):
            r +=1
        if (l <0)and (r >=lenn):
            i +=1
        else:
            if (nums[i]>nums[l])and(nums[i]>nums[r]):
                summ +=1
            elif(nums[i]<nums[l])and(nums[i]<nums[r]):
                summ +=1
            else:
                i+=1
        i = r
    return summ
        
print(x(nums))