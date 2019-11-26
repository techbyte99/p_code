d='y'
while (d=='y' or d=='Y'):
    n=int(input("enter the no.  but do not enter zero   "))
    sum=0
    temp=n
    while temp>0:
    
        digit=temp%10
        sum += digit**3
        temp=temp//10
    if n==sum:
        
        print(n,",this is an  armstrong number")
    else:
        
        print(n,",this is not an armstrong number")
    d=input("do you wanna continue[Y|N]")
if (d!='y' or d!='Y'):
    print("you are exited")