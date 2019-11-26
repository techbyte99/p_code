d='y'
while(d=='y' or d=='Y'):
    
    a=int(input("enter 1 for character to ascii value\nenter 2 for ascii value  to character "))
    if a==1:
        c=input("enter a character")
        print("ascii value is",ord(c))
    elif a==2:
        b=int(input("enter a integer value max of 6 digits"))
        print("character is",chr(b))
    d=input("do you wanna Ycontinue{y|n}")
if (d!='y' or d!='y'):
    print("you are exited")
    