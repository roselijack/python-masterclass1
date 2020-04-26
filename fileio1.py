#c111
# cities = ["abc","df2"]
# with open("cities.txt","w") as city_file:#如果文件不存在，则创建。如果文件存在，则覆盖
#     for city in cities:
#         print(city,file = city_file,flush=True) #表明结果输出到文件，city_file属于named arguments，"="左右两侧尽量不要有空格

# cities = []
# with open("cities.txt",'r') as city:
#     for i in city:#返回1个字符串列表。每1行为列表的1个元素，含有\n。
#         cities.append(i.strip("\n")) #去掉字符串末尾的\n。如果需要移除末尾的"abc",但是在末尾只有"ab",则会移去"ab"
# print(cities)
# for i in cities:
#     print(i)

# \n
# \r\n
# CR-LF
# imelda = "more","iml","2011",(
#     (1,"df"),(2,"dsf"))
# print(imelda)
# with open("imelda3.txt", 'w') as imelda_file:
#     #method1
#     # for i in imelda:
#     #     print(i, file=imelda_file)#imelda3.txt有四行，每个元祖占一行
#     #method2
#     print(imelda,file=imelda_file)#imelda3.txt有1行，包含4个元祖

    #print(imelda, file="imelda_file")AttributeError: 'str' object has no attribute 'write'


with open("imelda3.txt","r") as imelda_file:
    contents = imelda_file.readline()
print(type(contents))#<class 'str'>
imelda = eval(contents)#把string变为turple，实际工作中读入外部的数据不提倡用eval,因为可能外部文件还有非法指令而被执行，影响安全性
print(type(imelda))#<class 'tuple'>
#title,artist,year,tracks = contents，会报错，ValueError: too many values to unpack (expected 4)
title,artist,year,tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
