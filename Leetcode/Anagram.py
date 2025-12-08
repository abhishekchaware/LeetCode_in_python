s = "rat"
t = "car"
def anagram(s,t):
    if len(s) != len(t):
        return False
    sd= {}
    td ={}
    for i in range(len(s)):
        if s[i] not in sd :
            sd[s[i]]=1
        else:
            sd[s[i]] +=1
    for i in range(len(t)):
        if t[i] not in td:
            td[t[i]]=1
        else:
            td[t[i]] +=1
    if td == sd :
        return True
    else:
        return False 
print(anagram(s,t))
    