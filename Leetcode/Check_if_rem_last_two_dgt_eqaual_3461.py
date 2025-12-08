s = "3902"

while len(s) > 2:
    s1 =""
    for i in range(len(s)-1):
        res = (int(s[i])+int(s[i+1])) %10
        s1 +=str(res)
    s =s1 
print(s)