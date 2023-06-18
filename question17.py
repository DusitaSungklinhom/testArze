# word = str(input("Enter your word"))
# words = str(input("Enter your words"))
# passage = str(input("Enter your passage"))
# if len(word)> len(words) and len(words)> len(passage):
#     print(len(word))
# elif len(words)> len(word) and len(words)> len(passage):
#     print(len(words))
# elif len(passage)> len(word) and len(passage)> len(words):
#     print(len(passage))

# if len(word)==len(words)and len(word)==len(passage):
#     print("All the same")
# if len(word)==len(words)and len(word)!=len(passage):
#     print("Neither")
# elif len(words)==len(word)and len(words)!=len(passage):
#      print("Neither")
# elif len(passage)==len(word)and len(passage)!=len(words):
#     print("Neither")
string1 = input("กรอกสายอักขระที่ 1: ")
string2 = input("กรอกสายอักขระที่ 2: ")
string3 = input("กรอกสายอักขระที่ 3: ")

length1 = len(string1)
length2 = len(string2)
length3 = len(string3)

if length1 == length2 == length3:
    print("All the same")
elif length1 == length2 or length1 == length3 or length2 == length3:
    print("Neither")
else:
    max_length = max(length1, length2, length3)
    print(max_length)
