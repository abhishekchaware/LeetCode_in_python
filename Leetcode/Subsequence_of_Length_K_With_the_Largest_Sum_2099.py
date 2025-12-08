nums =[-1,-2,3,4]
k = 3
def max_k_val(nums,k):
    d={}
    l=[]
    lenn = len(nums)
    for i in range(lenn):
        d[i] = nums[i]
    sd = sorted(d.items(),key=lambda x:x[1],reverse=True)
    topk = sd[:k]
    topk.sort(key=lambda x:x[0])
    for i in range(len(topk)):
        l.append(topk[i][1])
    return l
print(max_k_val(nums,k))