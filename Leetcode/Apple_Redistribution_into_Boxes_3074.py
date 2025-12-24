
def minimumBoxes(apple ,capacity) -> int:
    applesum = sum(apple)
    lenn = len(capacity)
    summ =0
    cap =0
    lst = sorted(capacity,key=lambda x:-x)
    for c in range(lenn):
        cap +=lst[c]
        summ +=1
        if cap >=applesum:
            break
    return summ

apple = [1,3,2]
capacity = [4,3,1,5,2]
print(minimumBoxes(apple,capacity))