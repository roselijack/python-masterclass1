
activity = input("what to do like to do?")
if "cinema" in activity.casefold(): # in: 子字符串是否包含在某字符串中。 casefold:转化为小些，比lowercase好。比如德语中小写有好几种写法
    print("i'll go to the cinema")
else:
    print("i will not go to the cinema")