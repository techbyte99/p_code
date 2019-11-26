import pandas as pd
data=pd.DataFrame({'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],
'Address':['Delhi','Kanpur','Allahabad','Kannauj'],'Qualification':['Msc','MA','MCA','Phd']})
print(data)
print(data.describe())
height=[5.1,5.6,5.2,4.9]
data['Height']=height
print(data)
