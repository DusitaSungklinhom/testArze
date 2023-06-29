# N = int(input("Enter your number"))
# for i in range (N):

    
N = int(input("ป้อนจำนวนเต็ม N: ")) #5
sum = 0

for i in range(1,N+1):
    sum += i ** 2

print("ผลรวมของเลข N ล่าสุดที่ยกกำลังสองคือ:", sum)