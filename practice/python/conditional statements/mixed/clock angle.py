h=int(input("enter hour(1-12):"))
m=int(input("enter minutes (0-59):"))
mang= m*6
hang= h*30+mang
angle = (hang-mang)
if angle > 180:
    smallerangle= 360-angle
    print("the smaller angle is ",smallerangle)
else: 
    print("the smaller angle is ",angle)
