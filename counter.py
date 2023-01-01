#2.3 Counter
def counter(number):
    message = ""
    for i in range(0,number+1):
        message += str(i) + '\n'
        #print(message)
    return message 

count = input('Enter a number: ')
number = int(count)

print(counter(number))
