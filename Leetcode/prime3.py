num = int(input("enter the number here: "))
def is_prime(n):
    if n <1:
        return "enter no. greater than 1"
    else:
        if n ==2:
            return n 
        for i in range(2,n//2):
            if n %i ==0:
                return "not prime"
            else:
                return "prime"
print(is_prime(num))