'''
Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3
'''
points = [[1,0],[2,0],[3,0],[2,2],[3,2]]


def  trapezoid(points):
    y = []
    x =[]
    summ = 0
    for i in range(len(points)):
        y.append(points[i][1])
        x.append(points[i][0])

    y_sett = set(y)
    x_sett = set(x)
    n1 = len(x_sett)
    n2 = len(y_sett)
    num1 = n1*(n1-1)//2
    num2 = n2 *(n2-1)//2
    res = num1 * num2
    return res
    
            

print(trapezoid(points))

v = [0, 0, 0, 2, 2]
x = 0
lenn = len(v)
while x < lenn:
    if v[x]==0:
        v.pop(x)
        lenn -=1
    else:
        x +=1
print(v)