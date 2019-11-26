n=5
k=4
for i in range(n,0,-1):
    print(k*'\t',end="\t")
    for j in range(i,n+1):
        print(j,end="\t")
    k-=1
    print('\n')
