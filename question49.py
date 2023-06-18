number = int(input("Enter your number:"))

output = ""

for i in range(1, number + 1):
    output += str(i)

for i in range(number):
    print(output[:len(output)-i])


