def sumzro(n):
    l1=[]
    for i in range(1,n//2+1):
        l1.append(i)
        l1.append(-i)
    if n % 2 ==1:
        l1.append(0)
    return l1
print(sumzro(5))