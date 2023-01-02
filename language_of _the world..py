#3.3 Language of the word.
def language_of_the_word(word):
    if word.endswith("cion"):
        answer = "Spanish!"
    elif word.endswith("tion"):
        answer = "English!"
    elif word.endswith("zio"):
        answer = "Basque!"
    else:
        answer =  "Ups....I don't know!"
    return answer

word = input("I bet I hit the language!")
print(language_of_the_word(word)) 

