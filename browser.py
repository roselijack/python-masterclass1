import webbrowser
#webbrowser.open("https://www.python.org",new=3) #用默认的浏览器打开url。new的值用于区分是新开个窗口还是新开个页签，不一定生效。
#webbrowser.get('/usr/bin/google')
# help(webbrowser)

# for i in range(10):
#     print(1,2,3,sep=';',end='5')#sep=';'表示1，2，3间用分号隔开，end=5表示每次print语句执行完后加上后缀5。输出结果1;2;351;2;35
#

#chrome = webbrowser.get('/usr/bin/google-chrome %s').open("https://www.python.org")#.Error: could not locate runnable browser
webbrowser.get(using='safari').open("https://www.python.org")


