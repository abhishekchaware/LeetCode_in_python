"""
    Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
s = ["h","e","l","l","o"]

def reverse_string_inplace(s):
    lenn = len(s)
    l=0
    r = lenn-1
    while (l <r):
        s[l],s[r] = s[r],s[l]
        l +=1
        r -=1
    return s

print(reverse_string_inplace(s))