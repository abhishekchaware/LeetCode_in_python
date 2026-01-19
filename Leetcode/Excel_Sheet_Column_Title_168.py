def convertToTitle(columnNumber):
    s = 'abcdefghijklmnopqrstuvwxyz'
    d={}
    lenn =len(s)
    for i in range(lenn):
        si=s[i].upper()
        d[i+1]=si
    res =""
    tmp =columnNumber
    while tmp >0:
        rem = tmp %26
        if rem==0:
            rem = 26
            tmp //=26
            tmp -=1
        else:
            tmp //=26
        res =d[rem]+res
    return res  
        

columnNumber = 701
print(convertToTitle(columnNumber))
