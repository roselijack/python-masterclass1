# 打开文件
# 读文件
# 关闭文件
#method1
# jaccob = open("sample.txt","r") #默认路径为该python文件所在目录
# for line in jaccob:
#     if "jabberwock" in line.casefold():
#         print(line,end='')#不加end='',则每行输出后均有1行空格
#
# jaccob.close()

#method2
# with open("sample.txt","r") as jaccod :
#     for line in jaccod:
#         if "JAB" in line.upper():
#             print(line,end='')
#method3
# with open("sample.txt","r") as jaccod:
#     line = jaccod.readline()
#     while line: #如果读到文件最后了，读取的内容为空，则不进入while loop
#         print(line,end='')
#         line= jaccod.readline()
#method4
# with open("sample.txt","r") as jaccod:
#     lines = jaccod.readlines() #调试时用，返回1个list of strings,包含文件第一行到最后1行内容。含\n。耗内存，把内容一次性读入，每一行末尾有\n。
# print(lines)
#
#
# # for line in lines:
# #     print(line,end='')#先打印第1行的内容，最后打印最后一行内容
#
# for line in lines[::-1]:
#     print(line,end='')#先打印最后1行的内容，最后打印第一行内容
#method5
with open("sample.txt","r") as jaccod:
    line = jaccod.read() #一次性读入所有内容，没有换行符,返回a single string
print(line)
for a in line[::-1]:#
    print(a,end='')#如果是print(a),则将line中每个字符1个1个的换行打印，加上end=''能去掉换行符

#readlines: return a list of strings
#readline reads a single line from a file and returns a string
#read: reads entire files,if it's a text file returns a string containing the contents of the file,能够加上读多少数据的参数


