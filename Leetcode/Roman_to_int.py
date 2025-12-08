num =input("enter the roman numbers here: ").upper()
def romanToInt(s:str)-> int:
        roman= {'I':1, 'V':5, 'X':10, 'L':5,'C':100, 'D':500, 'M':1000}
        
        result = 0
        for i in range(len(s)):
            curr = roman[s[i]]
            if i + 1 < len(s):
                next_val = roman[s[i+1]]
            else:
                next_val = 0
            
            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result
print(romanToInt(num))