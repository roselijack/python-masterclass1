import shelve
blt = ["a","b","c"]
beans = ["d","e"]
scramble = ["f","g","h"]

# recipe = shelve.open("recipes")
# recipe["blt"] = blt
# recipe["beans"] = beans
# recipe["scramble"] = blt
# recipe.close()

with shelve.open("recipes",writeback=True) as recipe:#writeback能将内存中的内容即时写入disk
# blt.append("c1") #此步无法更新recipe["blt"]
# # recipe["blt"] = blt #此步可以更新recipe["blt"]
    recipe["blt"]=["dfe"]
    recipe.sync() #强制将内容写入disk
    blt.append("dfe1")
    for i in recipe.keys():
        print(i,recipe[i])

        



