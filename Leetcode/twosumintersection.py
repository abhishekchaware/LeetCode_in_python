nums1 = [1,2,2,1]
nums2 = [2,2]
def tsi(nums1,nums2):
    s = set(nums1)
    s1 = set(nums2)
    i = s.intersection(s1)
    return list(i)
print(tsi(nums1,nums2))