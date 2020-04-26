#c113
# with open("binary","bw") as bin_file:
    #方法一
#     # for i in range(17):
#     #     bin_file.write(bytes([i]))#1.如果写成bytes(i),it creates a bite sequence with that many bites all set to zero.加上[]变为list,将list转变为二进制
#
#     #方法二
#     bin_file.write(bytes(range(17)))
# with open("binary","br") as binFile:
#     for b in binFile:
#         print(b)
#

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2","bw") as bin_file:
    #bin_file.write(bytes([a]))#a = 65534,ValueError: bytes must be in range(0, 256)
    bin_file.write(a.to_bytes(2,"big"))#to_bytes，将整数转为二进制。第一个参数是转换后的字节数据长度，第二个参数 byteorder 将字节顺序定义为 little 或 big-endian，可选参数 signed 确定是否使用二进制补码来表示整数。
    bin_file.write(b.to_bytes(2,"big"))#
    bin_file.write(c.to_bytes(4,"big"))
    bin_file.write(x.to_bytes(4,"big"))
    bin_file.write(x.to_bytes(4,"little"))

with open("binary2","br") as bin_file:
    a1 = int.from_bytes(bin_file.read(2),"big")#int.from_bytes。把bytes类型的变量x，转化为十进制整数。bin_file.read(2)表示读取两个字节。
    b1 = int.from_bytes(bin_file.read(2),"big")
    c1 = int.from_bytes(bin_file.read(4),"big")
    x1 = int.from_bytes(bin_file.read(4),"big")
    x2 = int.from_bytes(bin_file.read(4),"big")
    print(a1)
    print(b1)
    print(c1)
    print(x1)
    print(x2)



