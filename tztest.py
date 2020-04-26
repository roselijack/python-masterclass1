import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
print(type(tz_to_display))
local_time = datetime.datetime.now(tz=tz_to_display)
print("the time in {} is {}".format(country,local_time))
print("the time is {}".format(datetime.datetime.utcnow()))
print("the time is {}".format(datetime.datetime.now()))


# for x in pytz.country_names:   #<class 'pytz._CountryNameDict'>
#     print(x+":"+pytz.country_names[x]) #CN:China
# print(type(pytz.country_names))
# print(type(pytz.all_timezones))#获取所有的时区
# for x in pytz.all_timezones:#huo
#
#     print(x)
#
# for i in list(range(10)):
#     print("xxx")

# for i in pytz.country_timezones:
#     print(i)#NO BV
# for x in sorted(pytz.country_names): #条件断点：此处如果条件为x=='BV',不生效。此处x不被识别
#     country_full_name = pytz.country_names[x]#条件断点：此处x=='BV'条件断点生效。即仅当x='BV'时断点才生效
#
#     if x in pytz.country_timezones:
#         for y in sorted(pytz.country_timezones.get(x)):
#             print(country_full_name+":"+y+":"+str(datetime.datetime.now(tz=pytz.timezone(y)))) #需要pytz.timezone(x)把字符串类型的时区转变为datetime.tzinfo


# pytz.country_names #<class 'pytz._CountryNameDict'>key:CN,value:China
# pytz.country_timezones#dict,key:CN,value:该国家对应的timezone列表。一个国家可能有多个时区
# pytz.timezone(zone)#通过字符串获取datetime.tzinfo。传入datetime.datetime.now(tz=pytz.timezone(zone))
# pytz.all_timezones#获取所有的时区
