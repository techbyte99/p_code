d='y'
while (d=='Y'or d=='y'):
 a=int(input("enter the value of a = "))
 b=int(input("enter the value of b = "))
 c=int(input("enter the value of c = "))
 if a>b and a>c:
    print("the maximum no. is",a)
 elif b>a and b>c:
    print("the maximum no. is",b)
 else:
    print("the maximum no. is",c)
 d=input("do you want to continue[Y/N]")
if d!='y'or d!='Y':
 print("you are exited")
    
