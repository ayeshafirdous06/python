n=int(input("Enter number:"))
original =n
sum = 0
for i in range(n):
    digit = n%10
    sum= sum+digit**3
    n= n//10
if sum==original:
    print("Armstrong Number")
else:
    print("not an Armstrong")
