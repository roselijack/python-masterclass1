import random

hightest = 10
answer = random.randint(1,hightest)
#print(answer)

print("please guess number between 1 and {}:".format(hightest))
guess = ""
while(guess != answer):
    guess = int(input())
    if guess==0:
        print("quit")
        break
    elif(guess > answer):
        print("please guess lower")
    elif(guess<answer):
        print("please guess higher")
    else:
        print("well done")





