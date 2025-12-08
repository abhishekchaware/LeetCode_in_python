st= ["flower","flow","flight"]
def longet_common_prefix(st):
    f = st[0]
    rem = st[1:]
    l = len(f)
    for i in range(l):
        char = f[i]
        for word in rem:
            if  i ==len(word) or char !=word[i]:
                return f[:i]
    return f

print(longet_common_prefix(st))