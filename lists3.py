egg = []
egg.append(["1","2","3"])
egg.append(["1","2","4"])
egg.append(["1","2","10"])
egg.append(["5","2","10"])
for a in egg:
    if not "5" in a:
        print(a)
        for b in a:
            print(b)