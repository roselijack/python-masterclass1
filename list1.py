list_1 = []
list_2 = list()#用list构造函数构造一个空列表
print("list_1:{}".format(list_1))
print("list_2:{}".format(list_2))

if list_1 == list_2:
    print("the lists are equal")

print(list("the lists are equal"))
even = [2,4,6,8]
odd = [1,3,5,7]
numbers = [even,odd]#list numbers包含两个list, even和odd
print("numbers:{}".format(numbers))
for i in numbers:
    print(i)
    for a in i:
        print(a)
#another_even = even
another_even = sorted(even,reverse=False)
print("another_even-->{}".format(another_even))
print(another_even == even)
print(another_even is even)
second_even = list(even)
print(second_even == even)
print(second_even is even)
even.sort(reverse=True)
print("even-->{}".format(even))

#==指内容是否一致，is指地址是否一致

