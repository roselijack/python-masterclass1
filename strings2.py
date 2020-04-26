parrot = "Norwegian"
print(parrot)
print(parrot[3-9])
print(parrot[4-9])
print()
print(parrot[3-9])
print(parrot[6-9])
print(parrot[8-9])
print(parrot[-1])
print(parrot[-9])
print(parrot[0:9])
print(parrot[:9])
print(parrot[0:])
print()
print(parrot[:3]+parrot[3:])
print(parrot[:])

print(parrot[-3:-1])
print()
print(parrot[0:6:3])
print(parrot[0:6:2])
#number = "9,223;372:036 854,775;807"
number = input("please input number")
sep = ""
for character in number:
    if not character.isnumeric():
        sep = sep + character
print("sep--->>>>"+sep)
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))

letter = "abcdefghijklmnopqrstuvwxyz"
print(letter[25::-1])
print(letter[25:0:-1])
print(letter[-10:-13:-1])
print(letter[-22::-1])
print("this-->"+letter[:-9:-1])


print(letter[-4:])#打印倒数第四个字符到最后一个字符
print(letter[:1]) #打印第一个字符，如果letter为空，不会报错
print(letter[0])#打印第一个字符，如果letter为空，不会报错

letter1 = ""
print(letter1[:1])
print(letter1[0])




