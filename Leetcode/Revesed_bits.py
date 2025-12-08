'''
Input: n = 43261596

Output: 964176192
'''
def rev_bits(n):
    res =""
    tmp = n
    while tmp > 0:
        res += str(tmp%2)
        tmp //=2
    res = res.ljust(32,'0')
    rev = res[::-1]
    j = 0
    lenn = len(rev)
    val =0
    while j < lenn:
        bit = int(rev[j])
        val +=bit *(2**j)
        j +=1
    return val

n= 43261596
print(rev_bits(n))
print(n.bit_length())
n1 =5
i= len(bin(n1)[2:])
print(i)
r =""
while i >=0:
    r +=str((n1 << i)& 1)
    i -= 1
print(r)