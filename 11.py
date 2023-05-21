fr = open("store.txt", "r", encoding="utf-8")
fw = open("discount.txt", "w", encoding="utf-8")
discount = None
for i in fr.readlines():
    price = None
    line_data = i.strip().split('\t')
    if len(line_data) >= 2:  # Check if the line contains both product name and price
        product = line_data[0].strip()
        price = int(line_data[1].strip())
    if price is not None:
        if price >= 10000:
            discount = price * 0.1
        else:
            discount = 0
    fw.write(product + "\t" + str(price) + "\t" + str(discount) + "\tpayment=" + str(price - discount) + "\n")
fw.close()
fr.close()


