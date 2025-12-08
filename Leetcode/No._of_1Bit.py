def check1(n):  
    res =""
    tmp = n
    while tmp > 0:
        res += str(tmp%2)
        tmp //=2
        
    i =0
    lenn = len(res)
    summ = 0
    while i < lenn:
        s='1'
        if res[i]==s:
            summ +=1
        i +=1
    return summ


# optimised code

n =4

print(check1(n))



