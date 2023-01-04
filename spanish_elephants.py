#4.8 spanish elephants in file.
def spanish_elephants_in_file(directory):
    fin=open(directory)
    message = ""
    letters = 1
    for line in fin: 
        line = line.lower()
        if "l" in line and "f" in line and "a" in line and "n" in line and "t" in line and line.count("e") >=3:
            message += "Spanish elephant is in this line: " + str(letters) +"\n"
        letters = letters+1
    fin.close()
    return message.strip()
print(spanish_elephants_in_file("sayings.txt"))