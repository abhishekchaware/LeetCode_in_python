num =int(input("enter the number here: "))
#num=[3,5,7]
def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n//2):
            if n % i ==0:
                return  False
    return True
# def test(num):
#     for i in num:
#         if not  is_prime(num[i]):
#             return False
#         return True
# def test(num):
#     # Use a generator expression to check if each number in 'nums' is prime, and return True if all are prime
#     return all(is_prime(i) for i in nums)
print(is_prime(num))
    