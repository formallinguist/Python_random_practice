#Word in the book
def look_for_word(word):
    file = open("book.txt", "r") 
    variable = []
    word_lower = word.lower()
    
    for element in file:
        variable.append(element.lower()) 
    file.close() 

    contador_line=0 
    message= "" 
    for line in variable:  
        contador_line=contador_line+1 
        if word_lower in line: 
            message+= "Found in line: "+  str(contador_line) +"\n"
    if message == "": 
                    
                    
        message = "Not found"
    return message
    
        
word = input("Word to search: ")
print(look_for_word(word))