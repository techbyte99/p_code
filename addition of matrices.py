import random
a = int(input("Enter a integer for aXa matrix"))
matA = []
print("Enter the elements row wise")
for i in range(a): # A for loop for row entries
    c =[]
    for j in range(a): # A for loop for column entries
        c.append(int(input()))
    matA.append(c)
for i in range(a):
    for j in range(a):
        print(matA[i][j], end = " ")
    print()
b = int(input("Enter a integer b for bXb matrix same as for the previous matrix beacuse for addition dimension for both matrices must be equal"))
matB = []
print("Enter the elements row wise")
for i in range(b): # A for loop for row entries
    d =[]
    for j in range(b): # A for loop for column entries
        d.append(int(input()))
    matB.append(d)
for i in range(b):
    for j in range(b):
        print(matB[i][j], end = " ")
    print()
result = [[random.random()for col in range(len(matA))]for row in range(len(matB))]
for i in range(len(matA)):
    for j in range(len(matA[0])):
        result[i][j] = matA[i][j] + matB[i][j]
for r in result:
    print(r)
    
