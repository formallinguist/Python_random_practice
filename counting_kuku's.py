#3.1 Text info.
def text_info(text):
    size_of_text = "Size of the text: "+ str(len(text)) + "\n"

    #text = text.lower()
    if text.isupper():
        case = "In upper case"
        
        if text.count("KUKU") >=1:
            number = "Number of kuku's:" + str(text.count("kuku")) + "\n"
        else:
             number = "No kuku this way" + "\n"

    elif text.islower(): 
        case = "In lower case"

        if text.count("kuku") >=1:
            number = "Number of kuku's:" + str(text.count("kuku")) + "\n"
        else:
             number = "No kuku this way" + "\n"

    else:
        case = "Both lower and upper case"

        text = text.lower()
        
        if text.count("kuku") >=1:
            number = "Number of kuku's:" + str(text.count("kuku")) + "\n"
        else:
             number = "No kuku this way" + "\n"

    answer = size_of_text + number + case

    return answer
    
text = input('Enter a text: ')

print(text_info(text))