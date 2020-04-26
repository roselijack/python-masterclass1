a = b = c =d = 12 #同时给多个元素赋相同值
print(c)
a,b = 12,13 #给不同的元素赋不同值
print(a,b)
a,b = b,a#交换a和b的值
print("a is {}".format(a))
print("b is {}".format(b))