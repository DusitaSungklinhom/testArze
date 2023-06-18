# a,b = [int(i) for i in input("Enter your number a,b: ").split()]
# #countodd = 0
# if a%2 == 0:
#     #a = a+1
#     for i in range (a,b):
#         if i==2:
#             print(i+1)
#         elif i !=2:
#             print(i+2)
#         elif i == (b-1):
#             print(i)
        


# else:
#     pass
# #for i in range (a,b):
    

a,b = [int(i) for i in input("Enter your number a,b: ").split()]

# หาเลขคี่ทั้งหมดระหว่าง a และ b
odd_numbers = []
for i in range(a, b + 1):
    if i % 2 != 0:
        odd_numbers.append(i)

# แสดงเลขคี่ทั้งหมด
for i in odd_numbers:
    print(i,end=" ")

# หาผลรวมของเลขคี่ทั้งหมด
sum_odd = sum(odd_numbers)

# แสดงผลรวม
print()
print(sum_odd)

