import cmath
#taking the coefficient(ax^2 +bX +c)
a=float(input('enter a :'))
b=float(input('enter b :'))
c=float(input('enter c :'))
d=(b**2)-(4*a*c)
x1= (-b-cmath.sqrt(d))/(2*a)
x2= (-b+cmath.sqrt(d))/(2*a)
print('the root are {},{}'.format(x1,x2) )