def add(*add):
    for i in range(len(add)):
        add += add[i] 
    return add
print(add)        