def math(*number):
    total = 0
    for i in range(len(number)):
        total += number[i]
    print("ผลบวก  = ", total)
def sub(num1,num2):
    print("ผลลบ =",(num1-num2))

def multiply(*numbers):
    total = 1
    for i in range(len(numbers)):
        total *= numbers[i]
    print("multiply = ", total)

def divided(num11,num22):
    print("quotient = ",(num11/num22))

def mod(num1,num2):
    print("mod = ",num1%num2)

def percent(num1,num2):
    print("indivisible = ",num1//num2)