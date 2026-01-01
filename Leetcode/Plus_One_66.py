'''
Docstring for Leetcode.Plus_One_66
Input: digits = [1,2,3]
Output: [1,2,4]

'''
digits = [1,2,3]
def Plusone(digits):
    s = ''.join(str(x) for x in digits)
    n =int(s)+1
    l=[]
    while n >0:
        t=n%10
        l.append(t)
        n //=10
    return l[::-1]

print(Plusone(digits))