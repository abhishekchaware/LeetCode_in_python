s = input("enter the string here: ")
an = input("enter the anagram for above string: ")
def is_anagramm(s,an):
    if len(s) != len(an):
        return False
    sort_s = sorted(s)
    sort_an = sorted(an)
    
    if sort_s == sort_an:
        return True
    return False
print(is_anagramm(s,an))