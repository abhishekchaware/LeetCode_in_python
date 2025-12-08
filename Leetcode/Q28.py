s = "c"
f = "c"
def check(s,f):
    sl = len(s)
    fl = len(f)
    for i in range(sl-fl+1):
        summ = s[i:i+fl]
        if summ ==f :
            return i
    return -1

print(check(s,f))