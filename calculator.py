#for addition
def add(x,y):
    return(print("your addition is: " ,x+y))
#for subtraction
def sub(x,y):
    return(print("your subtraction is: " ,x-y))
#for multiplication
def mul(x,y):
    return(print("your multiplication is: " ,x*y))
#for division
def div(x,y):
    return(print("your division is: " ,x/y))
#for remainder      
def mod(x,y):
    return(print("your remainder is: ",x%y)) 
#for maximum integer after division
def maxi(x,y):
    return(print("integer after division: ",x//y)) 
d='y'
while(d=='y' or d=='Y'):
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    c=int(input("enter your choice :\n1. for addition \n2. for subtraction \n3. for multiplication\n4. for division\n5. for remainder\n6. for // ", ))
    if c==1:
        add(a,b)
    elif c==2:
        sub(a,b)
    elif c==3:
        mul(a,b)
    elif c==4:
        div(a,b)
    elif c==5:
        mod(a,b)
    elif c==6:
        maxi(a,b)
         
    else:
        print("print enter between 1-6")
    d=input("do you want to continue[y|n]: ")
if(d!='y'or d!='Y'):
    print(" you are exited.")
    