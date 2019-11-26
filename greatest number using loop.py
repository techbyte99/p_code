n=int(input("Enter how many no. you want to check : "))
g=int(input("Enter the first number"))
for i in range(2,n+1):
    k=int(input("Enter the %i number : "%i))
    if k>g :
        g=k
print("The greatest number is ",g)
