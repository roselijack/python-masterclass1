choice = "_"
#while else:When a loop terminates normally, the else block is executed.
while  choice != "0":#当while True时，应该仔细阅读代码，找出while的退出条件，放在while语句中，这样程序更清晰
    if choice in "1234":
       print("you choose {}".format(choice))

    else:
        print("Please choose one option")
        print("1:\tlearn python")
        print("2:\tlearn java")
        print("3:\tlearn swimming")
        print("4:\tlearn to bed ")
        print("0:\texit")
    choice = input()


