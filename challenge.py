location = {0:"you are sitting, hehi",
            1:"you are standing",
            2:"you are in the hill",
            3:"you are inside",
            4:"you are in vallege",
            5:"you are in the forest"}
exits = {0:{"Q":0},#定义字典里的每一项是字典
        1: {"W":2,"E":3,"N":5,"S":4,"Q":0},
        2: {"N":5,"Q":0},
         3:{"W":1,"Q":0},
         4:{"N":1,"W":2,"Q":0},
         5:{"W":2,"S":1,"Q":0}}
#print(location[0].split())#split默认用空格分开
print(location[0].split(","))
print(" ".join(location[0].split()))#将split后的每个元素用空格相连
namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = { "QUIT":  "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST":  "E",
               "WEST":  "W",
               "ROAD": "1",
               "HILL": "2",
               "BUILDING": "3",
               "VALLEY": "4",
               "FOREST": "5" }
loc = 1
while True:
    print(exits[loc].keys())#dict_keys(['W', 'E', 'N', 'S', 'Q'])
    availableExits = ", ".join(exits[loc].keys())#获取字典类型里嵌套的字典的keys,并且把keys里面的除了最后一个key外其他每1个key后缀加上","
    print(location[loc])

    if loc == 0:
        break
    allexists = exits[loc].copy()#字典allexists内容和exits[loc]一样。改变allexists内容后exits[loc]内容不变化
    allexists.update(namedExits[loc])#allexists内容被改变，添加了dic "namedExits[loc]"内容，但返回为None
    print("-"*40)
    print(allexists.items())
    print("-"*40)
    print(exits[loc])
    print("-"*40)
    print(allexists.update(namedExits[loc]))
    direction = input("available exits are {}".format(allexists.keys())).upper()
    if len(direction)>1:

        words = direction.split()#这样只要输入的句子中包含有west,north,south,east就可以识别
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
        # if direction in vocabulary:
        #     direction = vocabulary[direction]
        # else:
        #     print("you can't go to that direction")

    if direction in allexists:
        loc = allexists[direction]
        print("loc:{}".format(loc))#不能写成print("loc:"+loc),不然会报错str不能和int相连接
    else:
        print("the direction isn't found")

        #veg.update(fruite),返回none,veg变化 ,
        #a.copy().a不变化，返回1个同样的b