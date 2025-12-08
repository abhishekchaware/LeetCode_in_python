n = int(input("enter the number: "))
rev =0
temp =n
l = len(str(n))
for i in range(l):
    res=n%10
    rev =res
    temp//=10
    
print(rev)