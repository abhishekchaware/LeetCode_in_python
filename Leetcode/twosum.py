
"""
class Solution:
    def srt_list(self,nums):
        if len(nums) <=1:
            return nums
        else:
            p =nums[0]
            l = []
            r =[]
            for i in range(1,len(nums)):
                if nums[i] < p :
                    l.append(nums[i])
                else:
                    r.append(nums[i])
        return self.srt_list(l) +[p] + self.srt_list(r)
    
    def twosum(self,nums,target):
        print(nums)
        left = 0
        right =len(nums)-1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                return left ,right
            elif target < curr:
                right -=1
            else:
                left +=1
        return list((left ,right))
s = Solution()

num1 = s.srt_list(nums=nums)
print(s.twosum(nums=num1,target=6))

""" 
"""

def ts(nums,tgt):
    d ={}
    for k,v in enumerate(nums):
        d[k]=v
        res =tgt - v
        if res in d:
            return [d[k]]
"""
nums =[3,2,4]
t =6
def ts(nums,t):
    d ={}
    for i in range(len(nums)):
        rem = t-nums[i]
        print(nums[i],rem)
        if rem not in d:
            d[nums[i]]=i
            print(d)
        else:
            return [d[rem],i]

print(ts(nums,t))