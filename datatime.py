# import time
# print("time:"+time.strftime('%c',time.gmtime(0)))#Thu Jan  1 00:00:00 1970
#
# print("the timezone is {0} with an offset of {1}".format(time.tzname[0],time.timezone))#the timezone is CST with an offset of -28800
#
# print("local time is "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#local time is 2020-04-19 18:32:19,比time.gmtime()快8小时
# print("utc time is "+time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))#utc time is 2020-04-19 10:32:1999
import datetime
print(datetime.datetime.today())#modlue,class,function。返回类型：datetime，Return the current local datetime, with tzinfo None.2020-04-19 18:54:49.003092，datetime.datetime.today()比datetime.datetime.utcnow()快8小时。
print(datetime.datetime.now())#Return the current local date and time.和datetime.datetime.today()相近，更精确，能够通过tzed info object来描述时区。tzinfo是个抽象类，需要开发来实现。
print(datetime.datetime.utcnow())#Return the current UTC date and time, with tzinfo None.