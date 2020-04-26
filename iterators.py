# a = "1234"
# b = iter(a)
# print("b--->{0}".format(b))
# print(b)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# #print(next(b))
# # for i in len(a):
# #     print(next(b))
# for char in a:
#     print(char)
#
# for char in iter(a):
#     print(char)

rose = "lihongzhen"
rose_it = iter(rose) #创建1个iterator object，指数据流中1次返回1个元素。支持iterable的对象叫做iterator,strings和lists均是iterable objects
for i in range(len(rose)):#不能写成for i in len(rose),会报错"int can't be iterable"
    print(next(rose_it))#输出iterator object的下一个元素

for i in rose:#系统内部创建了iter(rose)
    print(i)