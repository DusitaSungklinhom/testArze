# n = int(input())
# min = None
# for i in range (n):
#     N = int(input("Enter your number"))
#     if N < min:
#         min = N


#2421

n = int(input("ป้อนจำนวนเต็ม n: "))

min_value = None #1

for i in range(n):
    N = int(input("ป้อนจำนวนเต็ม: "))

    if min_value is None or N < min_value:
        min_value = N

print("ค่าน้อยที่สุดคือ:", min_value)
