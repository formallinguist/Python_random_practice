#3.6 Palindromes.
def palindrome(word_input):
    variable = word_input.lower()
    variable1 = variable.replace(" ","")
    message = ""
    for i in range(0, len(variable1)):  
        if variable1[i]==(variable1[len(variable1)-1-i]):
            message = "Good!"
        else:
            message = "No, you missed it..."
            return message
    return message

word_input=input("Do you know any palindrome? ")
print(palindrome(word_input))

