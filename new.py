# sum=0
# while True:
#     number = int(input("enter your number"))
#     sum +=number
#     if sum >500:
#         break
#     print(sum)



max,min = 0,10000
while True:
     number = int(input("enter your number"))
     if number<0:
         break
     if number>max:
        max=number
     if number<min:
         min=number

print(max)
print(min)


# last = int(input("enter your number"))
# for row in range(1,last+1):
#     for colum in range(1,row+1):
#         print(colum,end='')
#         print("")


# number = int(input("enter your number"))
# for row in range(number):
#     for colum in range(number):
#         print("#",end='')
# print("")      
# number = int(input("enter your number"))
# for row in range(number):
#     for colum in range(number):
#         if (row+colum)%2==0:
#             print("x",end='')
#         else:
#             print("o",end='')
#         print("")


# number = int(input("enter your number"))
# for row in range(number):
#     for colum in range(number):
#         if row==0 or row==number-1 or colum==0 or colum==number-1:
#             print("X",end='')
#         else:
#             print(" ",end='')
#     print(" ")

#เขียนโปรแกรมทายเลขลูกเต๋า
# import random 
# myrandom = random.randrange(1,7) #1,2,3,4,5,6
# k=0
# while True:
#   if k==3:
#      break
#   number = int(input("enter your number :"))
#   correct = (number==myrandom) #true / false
#   if correct:
#     print("ตอบถูกรับไปเลย 1ล้านบาท")
#     break
#   else:
#     print("เสียใจด้วย")
#   k+=1


# number = int(input("enter your money(not more than 20,000)"))
# if number >=20000:
#   if number == 1000:
#     print(number)
#   if number == 100:
#     print(number)
#   if number == 10:
#     print(number)


# h = int(input("enter your hour"))
# m = int(input("enter your minute"))
# s = int(input("enter your second"))
# h = h*3600
# m = m*60
# print(h+m+s)

# weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
# high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
# bmi = weight/(high**2)

# if bmi>=0 and bmi<18.0:
#     result="ผอม"
# elif bmi>=18.5 and bmi<=22.9:
#     result="สมส่วน"
# elif bmi>=23.0 and bmi<=24.9:
#     result="น้ำหนักเกิน"
# elif bmi>=25.0 and bmi<=29.9:
#     result="โรคอ้วน ระดับที่ 1"
# elif bmi>30:
#     result="โรคอ้วนระดับอันตราย"
# else :
#     result="ไม่ทราบค่าที่ชัดเจน"

# print("ค่า bmi = ", bmi ,"ทำนายว่า =",result)    


# shirt = int(input("enter your size"))
# if shirt >37:
#     print("XS")
# if shirt <37 and shirt >41:
#     print("S")
# if shirt <=41 and shirt >43:
#     print("M")
# if shirt <=43 and shirt >46:
#     print("L")
# if shirt <=46:
#     print("XL")

# print("Your shirt size is",shirt)

 
