num1,num2,num3 = [int(i) for i in input("Enter your number 1,2,3: ").split()]
if num1==num2==num3:
    print("All the same")
elif num1!=num2 and num2 !=num3 and num1 != num3:
    print("All different")
else :
    print("neither")
