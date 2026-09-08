h=int(input("Hours Worked:"))
p=int(input("Pay per hour:"))
if h<=40:
    salary=h*p
    print("salary:",salary)
elif h>40:
    extra= h-40
    overtime= 1.5*p
    salary=h*p
    salaryy= (40*p)+(extra*overtime)
    print("salary with your overtime is ",salaryy)
    print("where your salary is",salary,"\nand your over time is",overtime)
