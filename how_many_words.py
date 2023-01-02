#3.8 How many words.
def how_many_words():
    list = []
    words_input = input("word: ")

    while words_input != "":
        if words_input not in list:
            list.append(words_input)
        words_input = input("Word: ")

    if words_input == "":
        word_number = (len(list))
        text = f"You know {word_number} different words!"
        return text
        

print(how_many_words())

