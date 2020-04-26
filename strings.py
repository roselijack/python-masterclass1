print("today is a good day")
print('python is fun')
print("python's string")
print('we can include "que" in strings')
print("hello"+" world")
greeting = "hello"
name = input("input ")
print(greeting+' '+name)
print(name + f" is {greeting}") #将greeting替换为该变量的值
print(f"pi is {22/7:12.7f}") #打印出22/7的结果并且宽度(整数部分加小数点加小数部分)为12位且右对齐，小数点后面为7位
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[1:5])

a = ["abc","abbcd","abc123f"]
result = {}
for i in range(0,len(a)):
    if(len(a[i]) ==5):
        for j in range(0,len(a[i])):
            if(result.keys()):


