#3.2 Broken keyboard
def broken_keyboard(keys):
    keys = keys.replace("%%","a")
    if "###" in keys:
        keys = keys.replace("###","u")  
    keys = keys.replace("##","e")
    return("He meant : " + keys)
keys = input("What did he write? ")
print(broken_keyboard(keys))

