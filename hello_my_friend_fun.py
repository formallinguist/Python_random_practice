#1.6 Functions till now.
#2 hello_my_friend.
def hello_my_friend(name):
    text = 'Hello, my friend ' + name
    return text

name = input('what is your name?')
print(hello_my_friend(name))