for i in range(1,20):
    print("a{}".format(i))#range产生一系列数，包含开始值，不包含结束值。

for i in range(10,2,-2):
    print("b{}".format(i))#range如果开始值比结束值大时或者开始值比结束值小时，产生的一系列数据包含开始值，不包含结束值。

for i in range(10,2):#range默认步长为1，步长为整数时，开始值如果大于结束值，则输出为负数
    print("d{}".format(i))

for i in range(10):#range可以不填写startvalue,表示从0开始
    print("e{}".format(i))