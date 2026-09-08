x=float(input("Enter X co-ordinate:"))
y=float(input("Enter Y co-ordinate:"))
if x>0 and y>0:
    print((x,y),"lies in 1st quadrant")
elif x<0 and y>0:
    print((x,y),"lies in 2nd quadrant")
elif x<0 and y<0:
    print((x,y),"lies in 3rd quadrant")
elif x>0 and y<0:
    print((x,y),"lies in 4th quadrant")
