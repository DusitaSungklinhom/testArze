# number = int(input("Enter your number"))
# for i in range (number):
    

# def fibonacci(n):
#     if n <= 1: 
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# number = int(input("ป้อนจำนวนเต็มบวก: "))

# result = fibonacci(number)

# print("ค่า Fibonacci ของ", number, "คือ:", result)

def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("ป้อนจำนวนเต็มบวกหนึ่งจำนวน: "))

result = factorial(number)

print("ค่า factorial ของ", number, "คือ:", result)
