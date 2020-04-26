farm_animals = {"sheep","cow","hen"}#定义1个set
print(farm_animals)#打印set {'cow', 'sheep', 'hen'}
for animals in farm_animals:#set是个iterator object,可以进行迭代轮询
    print(animals)
print("="*40)

wild_animals = set(["lion","tiger"]) #用set构造函数来定义1个set,参数为list
print(wild_animals)
farm_animals.add("horse")#给set farm_animals中增加1个元素
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)


empty_set = set()#构造1个空的set
empty_set_2 = {}#此种无法构造1个空的set,仅能构造1个空字典
empty_set.add("a")#
#empty_set_2.add("a")由于构造时用empty_set_2 = {}，会被识别为字典类型。AttributeError: 'dict' object has no attribute 'add'

even = set(range(0,40,2))
squars_turple = (4,6,9,16,25)
squars = set(squars_turple)
print("-"*40)
print(even.union(squars))#默认是从小到大排序。输出的set的内容是排序后在even中存在或者在squars中存在的元素
print(squars.union(even))#默认是从小到大排序。与even.union(squars)相同
#print(sorted(even+squars))#TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print(sorted(squars+even))#TypeError: unsupported operand type(s) for +: 'set' and 'set'
print("*"*40)
#如下四行输出结果相同
print(sorted(even.intersection(squars)))#输出的set的内容是排序后在even中存在且在squars中存在的元素
print(sorted(squars.intersection(even)))#输出的set的内容是排序后在squars中存在且在even中存在的元素
print(sorted(even&squars))#输出的set的内容是排序后在squars中存在且在even中存在的元素，等同于even.intersection(squars)
print(sorted(squars&even))#等同于even.intersection(squars)

print("+"*40)
print(sorted(even.difference(squars)))#输出的set的内容是排序后在even中存在但是在squars中不存在的元素
print(sorted(even-squars))#输出的set的内容是排序后在even中存在但是在squars中不存在的元素，等同于even.difference(squars)
print(sorted(squars.difference(even)))#输出的set的内容是排序后在squars中存在但是在even中不存在的元素，不等同与even.difference(squars)
print(sorted(squars-even))#输出的set的内容是排序后在squars中存在但是在even中不存在的元素，等同于squars.difference(even)

print("="*40)
even ={0, 2, 4, 6, 8, 12, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38}
#even = set(range(0,40,2))
print(even)
print(squars)
print(even.symmetric_difference_update(squars))#返回None,even更改为在even和squars中不重复存在的元素
print(even)
print(even.symmetric_difference(squars))#返回两个集合中不重复(不同)的元素,even不变。
print(even)
even.difference_update(squars)#返回None,even更改为在even中存在但是在squars中不存在的元素，difference_update官方文档没有描述为排序。不能依赖与difference_update默认排序
print(even)
print(even.difference_update(squars))
print(sorted(even))#给set排序，返回排好序的list


print()

squars.discard(4) #移去squars中的4，如果4不存在，则不会报错，也不会做任何操作
squars.remove(16)
squars.discard(8)
#squars.remove(8)#移去squars中的8，如果8不存在，则会报错"KeyError: 8"
print(squars)
try:
    squars.remove(8)
except KeyError:
    print("rose")

if squars.issubset(even):
    print()
if even.issuperset(squars):
    print()

even = frozenset(range(0,100,2))#创建1个不能被改变的set,difference_update和symmetric_difference_update会报错。
print(even)

#even.add()#AttributeError: 'frozenset' object has no attribute 'add'
