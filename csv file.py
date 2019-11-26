import csv
fields=['NAME','BRANCH','YEAR','CGPA']
mydict={'NAME':'Nikhil','BRANCH':'COE','YEAR':'2','CGPA':'9.0'},{'NAME':'Sanchit','BRANCH':'COE','YEAR':'2','CGPA':'9.1'},
{'NAME':'Aditya','BRANCH':'IT','YEAR':'2','CGPA':'9.3'}, {'NAME':'Sagar','BRANCH':'SE','YEAR':'1','CGPA':'9.5'},{'NAME':'Prateek','BRANCH':'MCE','YEAR':'3','CGPA':'7.8'},
{'NAME':'Sahil','BRANCH':'EP','YEAR':'2','CGPA':'9.1'}
filename="university_records.csv"
with open(filename,'w',newline="")as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=fields)
writer.writeheader()
writer.writerows(mydict)
