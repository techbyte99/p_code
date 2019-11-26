import random
m1=int(input("Enter No. of rows in the first matrix: "))
n1=int(input("Enter No. of columns in the first matrix: "))
a = [[random.random() for col in range(n1)] for row in range(m1)]
for i in range(m1):
    for j in range(n1):
        a[i][j]=input()
m2=int(input ("Enter No. of rows in the second matrix: "))
n2=int(input ("Enter No. of columns in the second matrix: "))
b = [[random.random() for col in range(n2)] for row in range(m2)]
for i in range(m2):
    for j in range(n2):
        b[i][j]=input()
c=[[random.random()for col in range(n2)]for row in range(m1)]
print("multiplication matrix rowwise")
if (n1==m2):
    for i in range(m1):
        for j in range(n2):
            c[i][j]=0
            for k in range(n1):
               c[i][j]+=int(a[i][k])*int(b[k][j])
            print (c[i][j],end=" ")
    print()
else:
    print ("Multiplication not possible")
