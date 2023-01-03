#3.10 secret message

from re import X


def secret_message(text):
    list_1 = text.split()
    list_2 = []

    for word in list_1: 
        if word[0].isupper():
            word = word.lower()
            list_2.append(word)
    list_2.reverse()
    message = " ".join(list_2)
    return  f"message:{message}"
  

text = input("Code: ")
print(secret_message(text))
