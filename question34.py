countcalories=0
while True:
    print("1. Apple 100 Cal")
    print("2. Papaya 120 Cal")
    print("3. Banana 200 Cal")
    print("4. Orange 60 Cal")
    print("5. Exit")
    fruit = int(input("Enter your number"))  
    if fruit == 1:
        print("You choose Apple")
        countcalories+=100
    elif fruit ==2:
        print("You choose Papaya")
        countcalories+=120
    elif fruit ==3:
        print("You choose Banana")
        countcalories+=200
    elif fruit ==4:
        print("You choose orange")
        countcalories+=60
    elif fruit ==5:
        print("Bye Bye")
        break
print("Total Calories:",countcalories)