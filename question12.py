num1,num2,num3 = [int(i) for i in input("Enter your number 1,2,3: ").split()]
counteven = 0
countodd = 0
if num1%2 ==0:
    counteven +=1
else:
    countodd +=1
if num2%2 ==0:
    counteven +=1
else:
    countodd +=1
if num3%2 ==0:
    counteven +=1
else:
    countodd +=1
print("even",counteven)
print("odd",countodd)