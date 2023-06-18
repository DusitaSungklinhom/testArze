a = int(input())
ten = []
for i in range(a,-1,-1):
     if i % 10 == 0:
        ten.append(i)
for i in ten:
    print(i,end=" ")
# for i in range (number):
#     if number%10 ==1:
#         print(number)
