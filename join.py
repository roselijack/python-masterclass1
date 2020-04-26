myList = ["a","b","c","d"]
newString = ''
for c in myList:#写法1
    newString+=c+","
print(newString)#a,b,c,d,

new2 = ",".join(myList)#输出a,b,c,d。join不需要用在循环中。注意每个元素都后缀连接字符，但是最后一个元素不后缀连接字符。写法2，比写法1效率高，写法1每次都需要创建1个新字符串
print(new2)
print()#输出空行

new3 =  "1, ".join(myList)
print(new3) #a1, b1, c1, d。
# print()#输出空行
print(8+"abc")