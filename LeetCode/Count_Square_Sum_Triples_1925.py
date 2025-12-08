n=10
summ =0
l = set([k*k for k in range(1,n+1)])
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i*i) + (j*j)) in l:
            summ +=1
print(summ)