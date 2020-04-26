#c114
import pickle
#
imelda = ('more mayhem',
          'b',
          '2011',
          ((1,3),(2,4))
          )
even = list(range(0,10,2))
print(even)
odd = list(range(1,10,2))

with open("imelda.pickle",'wb') as imelda_pickle:
    pickle.dump(imelda,imelda_pickle,protocol=2)#将imelda内容变为二进制写入文件。不安全。第一个参数为要写入的数据，第二个参数为要写入的文件。
    pickle.dump(even,imelda_pickle,protocol=2)
    pickle.dump(odd,imelda_pickle,protocol=2)

with open("imelda.pickle","rb") as imelda_pickle:
    imelda1 = pickle.load(imelda_pickle)#从imelda_pickle中二进制的数据读取为重新构建的对象
    even1 = pickle.load(imelda_pickle)
    odd = pickle.load(imelda_pickle)
print(imelda1)
print(even)
print(odd)

