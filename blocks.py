age = int(input("age:"))#输入的需要是整数，不然报错
if age >= 18: #>=是个算术运算符
    print(age)
elif age == 3:
    print("rose")
else:
    print("please come back in {0} years".format(18-age))#format里可以是个表达式
