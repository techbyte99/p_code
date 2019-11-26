import math
def sin(x,n):
    sine=0
    for i in range(n):
        sign=(-1)**i
        pi=22/7
        a=x*(pi/180)
        sine=sine+((a**(2.0*i+1))/math.factorial(2*i+1))*sign
        return sine
print ("to find the expansion of sin(x,n)")
x=float(input("enter the value of x in degree: "))
n=int(input("enter the value of n: "))
print(round(sin(x,n),2))
