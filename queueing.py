import math
def sumr(c):
    List = []
    for i in range(c):
        List.append((r**i)/math.factorial(i))
    return List
print("Queueing Models : ","\n1. Single-Server Queues","\n2. Single Server Queues with Truncation"\
,"\n3. Multiserver Queues ","\n4. Multiserver Queues with Truncation")
m = int(input("Please Select any one Queueing Model(1/2/3/4) :"))
if(m == 1):
    la = float(input("Enter the Arrival Rate :"))
    mu = float(input("Enter the Service Rate :"))
    rho1 = la/mu
    l = rho1/(1-rho1)
    lq = (rho1**2)/(1-rho1)
    w = l/la
    wq = lq/la
    print("characteristics of queueing model ","\n1. Expected Number of the customers in the system: ",l,"\n2. Expected Number \
of the customers in the queue : ",lq,"\n3.Expected waiting time for the customer in system :",w,"\n4. Expected waiting time for \
the customer in the queue :",wq)
elif(m == 2):
    la = float(input("Enter the Arrival Rate :"))
    mu = float(input("Enter the Service Rate :"))
    rho1 = la/mu
    k = int(input("Enter the number of customers allowed in the system :"))
    if(round(rho1) == 1):
        pk = 1/(k+1)
        l = k/2
        lq = ((k**2)-k)/(2*(k+1))
        la_eff = la*(1-pk)
    else:
        pk = ((rho1**k)*(1-rho1))/(1-(rho1**(k+1)))
        l = rho1*((1-((k+1)*(rho1**k))+(k*(rho1**(k+1))))/((1-rho1)*(1-(rho1**(k+1)))))
        lq = (((k-1)*(rho1**(k+2)))-(k*(rho1**(k+1)))+(rho1**2))/((1-rho1)*(1-(rho1**(k+1))))
        la_eff = la*(1-pk)
        w = l/la_eff
        wq = lq/la_eff
        print("characteristics of queueing model ","\n1. Expected Number of the customers in the system: ",l,"\n2. Expected Number \
of the customers in the queue : ",lq,"\n3.Expected waiting time for the customer in system :",w,"\n4. Expected waiting time for \
the customer in the queue :",wq)
elif(m == 3):
    la = float(input("Enter the Arrival Rate :"))
    mu = float(input("Enter the Service Rate :"))
    c = int(input("Enter the number of servers :"))
    rho2 = la/(c*mu)
    r = la/mu
    p0 = 1/(((r**c)/(math.factorial(c)*(1-rho2)))+(sum(sumr(c))))
    l = r + (((r**c)*rho2)/(math.factorial(c)*((1-rho2)**2)))*p0
    lq = (((r**c)*rho2)/(math.factorial(c)*((1-rho2)**2)))*p0
    w = l/la
    wq = lq/la
    print("characteristics of queueing model ","\n1. Expected Number of the customers in the system: ",l,"\n2. Expected Number \
of the customers in the queue : ",lq,"\n3.Expected waiting time for the customer in system :",w,"\n4. Expected waiting time for \
the customer in the queue :",wq)
elif(m == 4):
    la = float(input("Enter the Arrival Rate :"))
    mu = float(input("Enter the Service Rate :"))
    c = int(input("Enter the number of servers :"))
    k = int(input("Enter the number of customers allowed in the system :"))
    rho2 = la/(c*mu)
    r = la/mu
    if(rho2 == 1):
        p0 = 1/((((r**c)/(math.factorial(c)))*(k-c+1))+(sum(sumr(c))))
    else:
        p0 = 1/((((r**c)*(1-(rho2**(k-c+1))))/(math.factorial(c)*(1-rho2)))+(sum(sumr(c))))
        lq = ((p0*(r**c)*rho2)/(math.factorial(c)*((1-rho2)**2)))*(1-(rho2**(k-c+1))-((1-rho2)*(k-c+1)*(rho2**(k-c))))
        pk = ((la**k)*p0)/((c**(k-c))*math.factorial(c)*(mu**k))
        l = lq + (r*(1-pk))
        la_eff = la*(1-pk)
        w = l/la_eff
        wq = lq/la_eff
        print("characteristics of queueing model ","\n1. Expected Number of the customers in the system: ",l,"\n2. Expected Number \
of the customers in the queue : ",lq,"\n3.Expected waiting time for the customer in system :",w,"\n4. Expected waiting time for \
the customer in the queue :",wq)
else:
    print("Invalid Option , Please select a valid option.")
