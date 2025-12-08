nums = [0,3,2,1,3,2]
def two_sneaky_num(nums):
    d ={}
    lst = []
    l = len(nums)
    for i in range(l):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] +=1
    for i,val in d.items():
        if val ==2:
            lst.append(i)
    lst.sort()
    return lst 

print(two_sneaky_num(nums))
