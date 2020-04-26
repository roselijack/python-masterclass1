#c116
import shelve

rose = {1:"rose",2:"jack"}
print(rose.items())
print(type(rose.items()))#<class 'dict_items'>
print(rose.keys())
print(type(rose.keys()))
print(rose.values())
print(type(rose.values()))

fruit = shelve.open("ShelfTest")

fruit["orange"] = "2"
fruit["pear"] = "3"
fruit["apple"] = "1"

print(fruit["pear"])
print(fruit["apple"])
fruit["lemon"] = "4"
print(type(fruit.items()))#<class 'collections.abc.ItemsView'>
print(fruit.items())#ItemsView(<shelve.DbfilenameShelf object at 0x10f942b70>)
print(fruit.keys())#KeysView(<shelve.DbfilenameShelf object at 0x10fb14b38>)
print(fruit.values())#ValuesView(<shelve.DbfilenameShelf object at 0x10fb14b38>)
for i in fruit.items():
    print(i)
print("-"*40)
for i in fruit.keys():
    print(i)
print("-"*40)
for i in fruit.values():
    print(i)
allkey = list(fruit.keys())#返回类型是<class 'collections.abc.KeysView'>，需要list()变为一个列表
allkey.sort()
print("-"*40)
for i in allkey:
    print(fruit[i])
while True:
    dict_key = input("please input a fruit")
    if dict_key == "quit":
        break
    else:
        description = fruit.get(dict_key,"the "+dict_key+" isn't found")
        print(description)
fruit.close()


#定义1个字典。print(type(rose.items()))#<class 'dict_items'>。
#定义1个shelve.print(type(fruit.items()))#<class 'collections.abc.ItemsView'>
#allkey = list(fruit.keys())#返回类型是<class 'collections.abc.KeysView'>，需要list()才能变为一个列表
#dictionary的key可以为任意类型。shelve的key只能为字符串
#可以不用with，而手动关闭shevle。fruit = shelve.open("ShelfTest")，接下里可以对fruit进行字典赋值。fruit.close()

