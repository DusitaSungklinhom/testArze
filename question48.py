# number = int(input("Enter your number"))
# count = 1
# for i in range (5):
#     print(1*count)
#     count+=1
#     if count>number:
#         break
number = int(input("Enter your number:"))

output = ""

for i in range(1, number + 1):
    output += str(i)
    print(output)