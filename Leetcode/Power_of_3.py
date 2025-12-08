num = int(input("enter the number here: "))
def pwf3(n : int)->bool:
    if n <=0:
        return False
    # if n % 3 !=0:
    #     return False
    while n% 3 ==0:
        n //=3
    if n==1:
        return True
    else:
        return False
print(pwf3(num))