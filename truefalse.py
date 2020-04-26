day = "sat"
temp = 10
raining = True
if day == "sat" and temp >27 or not raining: #and 优先级比or高，用括号更清晰
    print("swim")
else:
    print("")
if 0: #0代表False
    print("True")
else:
    print("False")
if "rose":
    print("rose is true")
else:
    print("rose is false")
if "":
    print("""""is true""")
else:
    print("""""is false""")

