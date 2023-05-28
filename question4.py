# integer = int(input("Enter your number"))
# numbers = int(input("Enter your number"))
# number = 1,2,3,4,5,6,7
# if number == 1:
#     print(integer + numbers)
    

n1,n2 = [int(i) for i in input().split()]
option = int(input())
result = 0

if option == 1:
    result = n1 + n2
elif option ==2:
    result = n1 - n2
elif option ==3:
    result = n1*n2
elif option ==4:
    result = n1/n2
elif option ==5:
    result =  n1%n2
elif option ==6:
    result = n1**n2
elif option ==7:
    result = (n1+n2)/2
else:
    print("Error")

if option !=5:
    print("%.5f" % result)
else:
    print(result)
