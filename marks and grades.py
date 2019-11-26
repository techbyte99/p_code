sub1=int(input("Enter marks of physics : "))
sub2=int(input("Enter marks of chemistry : "))
sub3=int(input("Enter marks of maths : "))
sub4=int(input("Enter marks of english : "))
sub5=int(input("Enter marks of physical education : "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
print("passing citeria>> less than 60% then student is fail")
