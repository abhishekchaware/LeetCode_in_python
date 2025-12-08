class Sol:
    def ReverseN()-> int:
        n = int(input("Enter the number: "))
        rev=int(str(abs(n))[::-1])
        if n == rev:
            print("The number is a ",n ,"Palindrome number")
        else:
            print(n,": its not a palindrome number")
# s = Sol()
# print(s.ReverseN()) 
Sol.ReverseN()