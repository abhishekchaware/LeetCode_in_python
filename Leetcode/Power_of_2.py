num = int(input("Enter the number here: "))
def pwr_of_2(n: int )->bool:
    if n <=0:
        return False
    if n %2 !=0:
        return False
    while n % 2 ==0:
        n //=2
    if n ==1:
        return True
    else:
        return False
    
print(pwr_of_2(num))