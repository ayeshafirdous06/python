cp=int(input("Cost Price:"))
sp=int(input("Selling Price:"))
if sp>cp:
    profit= sp-cp
    print("Profit of ",profit)
elif cp>sp:
    loss= cp-sp
    print("Loss of" ,loss)
elif sp==cp:
    print("no profit nor loss")
