a=float(input("Enter Total Balance: "))
w=float(input("Enter Withdrawal Amount: "))
balnce= a-w
minimumbal=1000
if balnce and a > minimumbal:
    totalbal=a-w
    print("Withdrawal approved, Remaining balance in your acc is",totalbal)
elif a < minimumbal:
    print("Withdrawal rejected, total balance less than minimum balance")
elif balnce < minimumbal:
    print("Total balance not equal to minimumbal try withdrawing less amount")
