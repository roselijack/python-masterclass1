decimal = range(0,100)
my_range = decimal[3:40:3]
print(my_range == range(3,40,3))#true
print(range(0,5,2)==range(0,6,2))#比较内容是否相等，尾标不同没有关系
r = range(0,100)
print(r)

for i in r[::2]:
    print(i)

print(('='*50))
for i in range(99,0,-2):
    print(i)
print(('+'*50))
for i in range(0,100,-2):#如果步长为负数则必须开始值比结束值大。否则range返回空。
    print(i)
print(('-'*50))
for i in range(99,0,-2):
    print(i)
print(range(0,100)[::-2] == range(99,0,-2)) #?range(0,100)[::-2]为空，range(99,0,-2)为99..97..1。这两个range为什么相等
for i in range(0,100)[::-2]:
    print("a"+str(i)) #结果为a99..a1，不为空
for i in range(99,0,-2):
    print("b"+str(i))
a = "rose"
print(a[::-1])

r = range(0,10)#[0,10)而不是[0,10]
for i in r[::-1]:
    print(i)
print(('*'*50))
o = range(0,100,4)
print(o)
p  = o[::5]
for i in p:
    print(i)