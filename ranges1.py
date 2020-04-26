my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))#返回字符e所在索引
print(my_string[4])

small_decimals = range(0,10)
print(range(0,10))#print range(0, 10)；而不是0..9
print(small_decimals.index(3))
odd = range(1,1000,2)
print("odd-->{}".format(odd))
print(odd)
print(odd.index(3))#注意index后面是(),不是[],返回数字3所在的位置
print(odd[3])#返回索引为3的位置的字符

sevens = range(7,1000,7)
x = int(input("please enter a number:"))
if x in sevens:
    print("the number can be divided by 7")

print(small_decimals)
my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))
decimal = range(0,100)
print(decimal)
my_range = decimal[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print(my_range == range(3,40,3))

decimal = range(0,100)
my_range = decimal[3:40:3]
print(my_range == range(3,40,3))#true