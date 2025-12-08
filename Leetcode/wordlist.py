wordlist = ["yellow"]
query = "YellOw"
s = set(wordlist)
l={}
for w in s:
    l[w.lower()]=w

print(l)