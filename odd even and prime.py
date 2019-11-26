def check(a):
    if (a%2)==0 :
        
        print("given no. is even")
    else:
        print("given no. is odd")        
def prime(a):
    if a > 1:
        for i in range(2,a):
            if (a % i) == 0:
              print(a,"is not a prime number")
              print(i,"times",a//i,"is",a)
              break
        else:
                print(a,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
    else:
        print(a,"is not a prime number")
   
d='y'
while(d=='y' or d=='Y'):  
    a=int(input("enter the no.:"))
    c=int(input(" enter 1 to check enen/odd \n enter 2 to check prime" ))
    if c==1:
       check(a)
    elif c==2:
         prime(a)
    d=input("do you want to continue[y|n]: ")
if(d!='y'or d!='Y'):
    print(" you are exited.")    
