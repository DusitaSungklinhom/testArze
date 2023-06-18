# number = int(input("Enter your number"))
# if number(len)==555:
#     print("hahaha")
# elif number(len)==555:
#     print("none")
number = input("กรอกตัวเลขความยาว 6 หลัก: ")

# ตรวจสอบว่าตัวเลขมีความยาว 6 หลักหรือไม่
if len(number) != 6:
    print("กรุณากรอกตัวเลขความยาว 6 หลัก")
else:
    # ตรวจสอบว่าตัวเลขเป็น "ตัวเลข hahaha" หรือไม่
    if "555" in number and number.count("5") == 3:
        print("hahaha")
    else:
        print("none")
