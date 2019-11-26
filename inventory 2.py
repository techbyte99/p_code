import math as m
class Inventory:
    def __init__(self,A,lmb,I,C,choice):
        self.A=A
        self.lmb=lmb
        self.I=I
        self.C=C
        self.choice=choice
    def model1(self):
        self.EOQ=m.sqrt((2*self.A*self.lmb)/(self.I*self.C))
        self.KC=m.sqrt(2*self.A*self.lmb*self.I*self.C)
        self.TC=(self.C*self.lmb)+self.KC

    def model2(self,si):
        self.si=si
        self.EOQ=m.sqrt((2*self.A*self.lmb*self.si)/(self.I*self.C*(self.si-self.lmb)))
        self.KC=m.sqrt(2*self.A*self.lmb*self.I*self.C*(self.si-self.lmb)/self.si)
        self.TC=(self.C*self.lmb)+self.KC

    def model3(self,S):
        self.S=S
        self.EOQ=m.sqrt((2*self.A*self.lmb*(self.I*self.C+self.S))/(self.I*self.C*self.S))
        self.KC=m.sqrt(2*self.A*self.lmb*self.I*self.C*self.S/(self.I*self.C+self.S))
        self.TC=(self.C*self.lmb)+self.KC

    def model4(self,si,S):
        self.si=si
        self.S=S
        self.EOQ=m.sqrt(((2*self.A*self.lmb*self.si*(self.I*self.C+self.S))/(self.I*self.C*self.S*(self.si-self.lmb))))
        self.MI=m.sqrt((2*self.A*self.lmb*(self.si-self.lmb)*self.S)/(self.I*self.C*self.si*(self.S+self.I*self.C)))
        self.MS=m.sqrt((2*self.A*self.lmb*(self.si-self.lmb)*self.I*self.C)/(self.S*self.si*(self.S+self.I*self.C)))
        self.KC=m.sqrt(2*self.A*self.lmb*self.I*self.C*self.S*(self.si-self.lmb)/self.si*(self.S+self.I*self.C))
        self.TC=(self.C*self.lmb)+self.KC
                        
    def display(self):
        print("EOQ is",self.EOQ)
        print("Total variable cost is",self.KC)
        print("Total cost is",self.TC)
        if(choice==4):
            print("Maximum inventory is",self.MI)
            print("Maximum shortage is",self.MS)
    

print("Menu\n1. model 1\n2. model 2\n3. model 3\n4. model 4")
check="Y"

while(check=='y' or check=='Y'):
    choice=int(input("Enter your choice : "))
    if(choice>0 and choice<5):
        A=float(input("Enter the ordering cost: "))
        lmb=float(input("Enter the Demand: "))
        I=float(input("Enter the Inventory carrying charge in percentage: "))
        I=I/100
        C=float(input("Enter the Unit cost: "))
        obj=Inventory(A,lmb,I,C,choice)
        if(choice==1):
            obj.model1()
            obj.display()
        elif(choice==2):
            si=float(input("Enter the Production Rate: "))
            obj.model2(si)
            obj.display()
        elif(choice==3):
            S=float(input("Enter the stockout cost: "))
            obj.model3(S)
            obj.display()
        else:
            si=float(input("Enter the Production Rate: "))
            S=float(input("Enter the stockout cost: "))
            obj.model4(si,S)
            obj.display()
    else:
        print("Enter the Right coice")
    check=input("Do you want to continue(Y/N) : ")
