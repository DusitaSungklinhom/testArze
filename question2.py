y1, m1, d1 = [int(x) for x in input("ป้อนค่า y1, m1, d1: ").split()]
y2, m2, d2 = [int(x) for x in input("ป้อนค่า y2, m2, d2: ").split()]
if y1>y2:
    print("2")
elif y2>y1:
    print("1")
elif y1==y2:
    if m1>m2:
        print("2")
    elif m2>m1:
        print("1")
    elif m1==m2:
        if d1>d2:
            print("2")
        elif d2>d1:
            print("1")
        elif d2==d1:
            print("equal")