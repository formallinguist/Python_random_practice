#2.1 First and last characters.

def first_and_last_characters(word):
    first_character = 'First character: '+ (word[0])
    last_character = '\nLast character: ' + (word[-1])
    first_last =  first_character +"\n"+ last_character
    return first_last
    
word = input('Enter a word: ')

print((first_and_last_characters(word)))