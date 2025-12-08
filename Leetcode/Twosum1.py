nums =[5,9,1,2,4,15,6,3]
t =13
def ts(nums,t):
    l=len(nums)
    for i in range(l-1):
        for j in range(i+1,l):
            print("i ",nums[i],"j ",nums[j])
            if nums[i] + nums[j] == t:
                return[i,j]
print(ts(nums,t))