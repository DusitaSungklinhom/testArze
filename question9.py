number = int(input("Enter your number"))
sign = input("Enter your sign")
reversed_number = int(str(number)[::-1])
if sign == "+":
    print(f"{number} {sign} {reversed_number} = {number+reversed_number}")
elif sign == '*':
    print(f"{number} {sign} {reversed_number} = {number*reversed_number}")
#print(number+sign+reversed_number)

