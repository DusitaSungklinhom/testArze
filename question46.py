number = int(input("Enter your number"))
count = number
while True:
    print("* "*count)
    count-=1
    if count == 0:
        break