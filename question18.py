# number = int(input("Enter your number"))
# if number :0:7 
# print("lucky")
# if number :0:7 == 5 or 9
#  print("Very lucky")
# else:
#  print("Usual")



number = input("กรุณาใส่ตัวเลข: ")

if number[0] == '9' and number[-1] == '9':
    print("Very Lucky")
elif number[0] == '5' and number[-1] == '5':
    print("Very Lucky")
elif number[0] == number[-1] :
    print("Lucky")
else:
    print("Usual")

