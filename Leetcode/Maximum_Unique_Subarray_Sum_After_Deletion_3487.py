def maxSum(l) -> int:
    if len(l)==1:
        return l[0]
    lenn = len(l)
    summ =0
    i=0
    count =0
    l1 =[]
    while i < lenn:
        if l[i] >0:
            count +=1
        if l[i] in l[i+1:]:
            l.remove(l[i])
            lenn -=1
        else:
            i +=1
    if count >=1:
        l1 =[x for x in l if x >0]
        return sum(l1)
    else:
        return max(l)

nums =[1,1,0,1,1]
print(maxSum(nums))