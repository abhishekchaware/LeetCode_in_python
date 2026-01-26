nums =[2,3,1,2,4,3]
t=7

def minSubArrayLen(nums,t):
    lenn  = len(nums)
    left =0
    summ =0
    minlen = float("inf")
    
    for right in range(lenn):
        summ += nums[right]
        
        while summ >=t:
            minlen = min(minlen,right-left+1)
            summ -=nums[left]
            left +=1
    if minlen == float("inf"):
        return 0
    return minlen

print(minSubArrayLen(nums=nums,t=t))