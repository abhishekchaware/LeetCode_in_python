grid =[[5,1,0],[-5,-5,-5]]

def countNegatives(g):
    lenn = len(g)
    summ =0
    for i in range(lenn):
        ilen = len(g[i])
        for j in range(ilen-1,-1,-1):
            if g[i][j]<0:
                summ +=1
            else:
                break
    return summ
    
print(countNegatives(grid))