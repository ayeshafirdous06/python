m=float(input("Enter Marks:"))
a=float(input("Enter Attendance:"))
f=float(input("Enter FamilyIncome:"))
if m>500 and a>75 and f<100000:
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")
