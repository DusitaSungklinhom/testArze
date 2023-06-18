counteven = 0
countodd = 0
while True  :
    number = int(input("Enter your number"))
    if number%2 ==0:
        counteven+=1
    if number%2 !=0:
        countodd+=1
    if number == -1:
        break
print(counteven)
print(countodd)