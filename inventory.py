import cmath
print("\n1. for simple EOQ model \n2. for model with finite production \n3. for model with shortages allowed and are fully backlogged \n4. for generalised model(1+2+3)")
n=int(input("enter the value of n:"))
if(n==4):
    A=float(input("Enter per order cost i.e A\n"))
    l=float(input("Enter Demand\n"))
    c=float(input("Enter cost per unit\n"))
    i=float(input("Enter Inventory carrying cost in percentage \n"))
    psi=float(input("Enter Production Rate \n"))
    pi=float(input("Enter Shortage cost per unit \n"))
    m1=2*(A*l/(i*c/100))
    m2=((i*c/100)+pi)/pi
    m3=(psi)/(psi-l)
    EOQ=cmath.sqrt(m1*m2*m3)
elif(n==3):
    A=float(input("Enter per order cost i.e A\n"))
    l=float(input("Enter Demand\n"))
    c=float(input("Enter cost per unit\n"))
    i=float(input("Enter Inventory carrying cost in percentage \n"))
    psi=float(input("Enter Production Rate \n"))
    m1=2*(A*l/(i*c/100))
    m3=(psi)/(psi-l)
    EOQ=cmath.sqrt(m1*m3)
elif(n==2):
    A=float(input("Enter per order cost i.e A\n"))
    l=float(input("Enter Demand\n"))
    c=float(input("Enter cost per unit\n"))
    i=float(input("Enter Inventory carrying cost in percentage \n"))
    pi=float(input("Enter Shortage cost per unit \n"))
    m1=2*(A*l/(i*c/100))
    m2=((i*c/100)+pi)/pi
    EOQ=cmath.sqrt(m1*m2)
elif(n==1):
    A=float(input("Enter per order cost i.e A\n"))
    l=float(input("Enter Demand\n"))
    c=float(input("Enter cost per unit\n"))
    i=float(input("Enter Inventory carrying cost in percentage \n"))
    m1=2*(A*l/(i*c/100))
    EOQ=cmath.sqrt(m1)
else:
    print("Wrong Choice , try again")
print("EOQ for your model is ",EOQ)
