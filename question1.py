unit=int(input("Enter your unit"))
print(unit)
price=int(input("Enter the price"))
print(price)
member=(input("y/n"))
Total = unit*price
Discount = 0
if member == "y":
    if Total<=500:
        Discount=0.1*Total
        print(Total)
        print(Discount)
        print(Total - Discount)
    elif Total>=500 and Total<=1000:
        Discount=0.15*Total
        print(Total)
        print(Discount)
        print(Total - Discount)
    elif Total>1000:
        Discount=0.2*Total
        print(Total)
        print(Discount)
        print(Total - Discount)
        
elif member == "n":
    if Total<=500:
        Discount=0.05*Total
        print(Total)
        print(Discount)
        print(Total - Discount)
    elif Total>=500 and Total<=1000:
        Discount=0.1*Total
        print(Total)
        print(Discount)
        print(Total - Discount)
    elif Total>1000:
        Discount=0.15*Total
        print(Total)
        print(Discount)
        print(Total - Discount) 
else:
    print("error")

