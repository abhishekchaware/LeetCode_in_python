'''
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]
Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]
'''
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

    

# def findx(nums,k,x):
#     l = len(nums)
#     d ={}
#     res =[]
#     summ =0
#     for  i in range(l-k+1):
#         win = nums[i:i+k]
#         print(win)
#         for  ele in win:
#             if ele not in d:
#                 d[ele] = 1
#             else:
#                 d[ele] +=1
#         print("d: ",d)
#         sot = dict(sorted(d.items() , key= lambda x: (x[-1])))
        
#         print("sort: ",sot)
                

# print(findx(nums,k,x))


l1 =[1,1,2,2,3,4]
d1={}
i=0
while i < len(l1):
    if l1[i] not in d1:
        d1[l1[i]] =1
    else:
        d1[l1[i]] +=1
    i +=1
x1=3
print(d1)