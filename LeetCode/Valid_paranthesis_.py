'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
s = "[()]"
def isvalid(s):
    st =[]
    d={'}':'{',']':'[',')':'('}
    for key in s:
        if key not in d:
            st.append(key)
        else:
            if not st:
                return False
            else:
                p = st.pop()
                if p != d[key]:
                    return False
    return not st

print(isvalid(s))
