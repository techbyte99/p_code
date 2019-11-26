#for reversing
def reverse(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    print('reverse of the no.is :',rev)
#for sum of a given number
def sum1(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    print("The total sum of digits is:",tot)
#for taking input from user
d='y'
while(d=='y' or d=='Y'):
    n=int(input('enter the number:'))
    print('enter - "reverse" for rreversing the no. \nenter "sum1" for sum of digits ')
    x=str(input())
    if x=='reverse':
        reverse(n)
    elif x=='sum1':
        sum1(n)
    d=input("do you want to continue[y|n]: ")
if(d!='y'or d!='Y'):
  print(" you are exited.")
  