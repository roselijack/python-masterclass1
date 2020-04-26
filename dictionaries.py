# fruit ={}
# print(fruit)
# print(fruit["key"])
# 赋新值
# 两个key一样,warn,不报错
# 删除1个key,del
# 清除dic, fruit.clear()
# key不存在，报错keyerror
# fruit.get(key)
# 判断key 是否在dic中
# if key in dic
fruit = {"apple":"a","orange":"b","lemon":"c","apple":"a1"}#定义1个字典,如果key apple 已存在，则将最后一次的value赋给key"apple",相当于新赋值。
print(fruit)#{'apple': 'a', 'orange': 'b', 'lemon': 'c'}输出1个字典
print(fruit["apple"])#输出字典fruit里key"apple"的value
del fruit["apple"]#删除字典fruit里key"apple"
print(fruit)
fruit.clear()#清除key，fruit为{}
print(fruit)
#print(fruit["rose"])#KeyError: 'rose'
print(fruit.get("rose"))#不报错，输出None
fruit = {"apple":"a","orange":"b","lemon":"c","apple":"a1"}#定义1个字典

while(True):
    choice = input("please type a fruit")
    #if choice in fruit.keys():#查找某key是否在字典里面
    # if choice in fruit:#等同于if choice in fruit.keys()，查找某key是否在字典里面
    #     print(fruit[choice])
    # elif choice == "quit":
    #     print("quit")
    #     break
    # else:
    #     print("this kind of fruit can'be found")
    if choice == "quit":
        print("quit")
        break
    else:
        print(fruit.get(choice,"no "+choice+"is found"))#当key "choice"不存在时，输出第二个参数



ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f+"-"+fruit[f])
for f in sorted(fruit.keys()):
    print(f+"-"+fruit[f])

for f in fruit:
    print(f+"++"+fruit[f]) #f为key，任何时候，能用key的地方不要用value,用key的效率更改

for f in fruit.values(): #
    print("------"+f)


# if fruit.has_key('apple'):#has_key是python2的语法，此句会报错AttributeError: 'dict' object has no attribute 'has_key'
#     print("========")
#用key时更高效，dict_keys,dict_value
#print("fruit.items()"+str(fruit.items()))#fruit.items()返回dict_items object
print(fruit.items())#dict_items([('apple', 'a1'), ('orange', 'b'), ('lemon', 'c')])
print(tuple(fruit.items()))#将dict_items object转换为标准的元祖，(('apple', 'a1'), ('orange', 'b'), ('lemon', 'c'))
for f in tuple(fruit.items()):#取出tuple(fruit.items())的每个元祖并unpacking
    a,b = f
    print(a+" is "+b)

#tuple(fruit.items())




