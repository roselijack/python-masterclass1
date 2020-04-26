
text = input("please input a string:")
textset = set(text)
vowels = {"a","o","i","u","e"}
results = sorted(textset.difference(vowels))
print(results)