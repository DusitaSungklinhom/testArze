number = input("Enter your number")
countnumber = 0
if len(number)>5:
    print("Too long")
elif len(number)<3:
    print("Too short")
elif len(number) == 3 or 4 or 5: 
    for i in number:
        if i == "1":
            countnumber += 1
    print(countnumber)

    
    
    
