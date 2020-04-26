#c115
#with 结束了，则fruit不生效
#文件名不能取名shelve
import shelve
with shelve.open("bike2") as bike:
    #出了with scope，则bike不能被识别为字典。在with外使用bike会报错ValueError: invalid operation on closed shelf
    bike["1"] = "benchi"
    bike["3"] = "baoma"
    for i in bike:
        print(i)
    print(bike["1"])
    print(bike["2"])

#如果文件名为shelve，代码shelve.open会报错：AttributeError: module 'shelve' has no attribute 'open'
#python文件重命名，右键文件->refactor->rename
#shelve是持久化存储数据。with shelve.open("bike2") as bike:
#bike2指定存储的数据库文件名为bike2.db。bike指定为存储内容的字典，接下来可以给该字典赋值
#一旦指定bike["3"] = "baoma"，则该key存在数据库中，即使下次没有给字典赋值给key,该key也在bike字典中一直存在。除非del bike["3"]。
#shelve也可以执行删除文件命令，不安全