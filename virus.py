#4.6 Virus
def virus(direction):
    variable = []
    text = open(direction)
    for line in text: 
        variable.append(line) 
    text.close()
    for element in variable:
        if element.startswith("VIRUS"):
            variable.remove(element) 
    file = open("correct.txt","w") 
    for i in variable: 
        file.write(i)  
    file.close()
    return file

print(virus("homework.txt"))

